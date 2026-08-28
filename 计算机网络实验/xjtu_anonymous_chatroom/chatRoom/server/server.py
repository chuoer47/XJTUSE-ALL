import os
import sys
import threading
import socket

from xjtu_anonymous_chatroom.chatRoom.server import config
from xjtu_anonymous_chatroom.database.initdb import initdb
from lib.cipher import encrypt_AESkey
from Crypto.Random import get_random_bytes
from datetime import datetime
from xjtu_anonymous_chatroom.database.SQL import *
from xjtu_anonymous_chatroom.database.connectdb import *

# 获取当前文件所在目录的路径
current_dir = os.path.dirname(os.path.abspath(__file__))

# 获取项目路径（父文件夹的父文件夹）
project_dir = os.path.dirname(os.path.dirname(current_dir))

# 将项目路径添加到sys.path中
sys.path.append(project_dir)
print(project_dir)
class Server:
    def __init__(self, host: str, port: int):
        self.clients = {}  # 用户字典
        self.work_thread = None  # 用户线程

        # 初始化socket
        self.host = host  # 初始化host
        self.port = port  # 初始化端口
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 启动TCP
        self.server.bind((host, port))  # 绑定
        self.server.listen()  # 阻塞式监听

        # 生成AESkey
        self.AESkey = get_random_bytes(24)  # 24位随机密钥，可以变化
        print('AESkey: {}'.format(self.AESkey))

    def __handle(self, client: socket.socket) -> None:
        """每个客户端的子线程实现"""
        while True:
            try:
                msg: bytes = client.recv(1024)
                # 数据库记录消息，不记录解密后的消息，保障了隐私
                conn, cur = getDB()
                data = (str(self.clients[client]), msg, datetime.now())
                cur.execute(insert_chat_logs, data)
                conn.commit()
                self.__broadcast(msg)
            except:
                # 记录数据库
                conn, cur = getDB()
                data = (str(datetime.now()), str(self.clients[client]))
                cur.execute(update_comer_record, data)
                conn.commit()
                # 将客户端从字典中删除
                t = self.clients[client]
                del self.clients[client]
                client.close()
                # 输出控制台
                print('{}已断开连接。'.format(t))
                return  # 结束该线程

    def __broadcast(self, msg):
        """广播消息的实现"""
        # 直接广播来自客户端的消息，确保端对端通信
        for client in self.clients.keys():
            client.send(msg)

    def run_service(self) -> None:
        """为每个客户端创建子线程并运行广播服务的实现"""
        print('服务器正在运行，地址：{}:{}'.format(self.host, self.port))
        while True:
            client, address = self.server.accept()
            # 将此客户端及其IP地址存储到字典clients中
            self.clients[client] = address
            # 将登录记录到数据库中
            conn, cur = getDB()
            data = (str(address), str(self.host) + ":" + str(self.port), str(datetime.now()))
            cur.execute(init_comer_record, data)
            conn.commit()
            # 控制台输出
            print('{}已连接。'.format(str(address)))

            # 接收RSC公钥并发送回AES密钥
            pubKeyPEM = bytes(client.recv(1024))
            encrypted_AESkey = encrypt_AESkey(self.AESkey, pubKeyPEM)
            client.send(bytes(encrypted_AESkey))

            # 启动广播消息的线程
            self.work_thread = threading.Thread(target=self.__handle, args=(client,))
            self.work_thread.start()


def main():
    server = Server(config.IP, int(config.port))
    server.run_service()


def input_thread():
    conn, cur = getDB()
    while True:
        user_input = input()  # 等待用户输入
        if user_input == 'reboot':
            print("Rebooting...")
            # 执行初始化
            initdb(conn, cur)
            print("over!")
        elif user_input == "exit":
            print("Exiting...")
            initdb(conn, cur)
            os._exit(1)


if __name__ == '__main__':
    # 创建并启动输入线程
    thread = threading.Thread(target=input_thread)
    thread.start()
    # 主线程继续执行其他操作
    # 初始化数据库
    conn, cur = getDB()
    initdb(conn, cur)
    # 开始进去程序
    main()
    # 等待输入线程结束
    thread.join()
