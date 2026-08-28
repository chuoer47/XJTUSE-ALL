import os
import socket
import sys
import threading

from lib.cipher import AESCipher
from network_lab.UDP.UDPconfig import *
from network_lab.UDP.database.SQL import add_user, find_user
from network_lab.UDP.database.connectdb import getDB
from network_lab.UDP.database.initdb import initdb
from network_lab.UDP.server import config

# 获取当前文件所在目录的路径
current_dir = os.path.dirname(os.path.abspath(__file__))

# 获取项目路径（父文件夹的父文件夹）
project_dir = os.path.dirname(os.path.dirname(current_dir))

# 将项目路径添加到sys.path中
sys.path.append(project_dir)


class Server:
    def __init__(self, host: str, port: int):
        self.clients = {}  # 用户字典
        self.work_thread = None  # 用户线程

        # 初始化socket
        self.host = host  # 初始化host
        self.port = port  # 初始化端口
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 启动UDP
        self.server.bind((host, port))  # 绑定

        # 生成AESkey
        self.AESkey = AESkey  # 写死的密钥
        self.cipher = AESCipher(self.AESkey)
        print('AESkey: {}'.format(self.AESkey))

    def __process(self, msg):
        require = self.__getRequire(msg)
        if require["type"] == "newUser":
            massage = self.__newUser(require)
        elif require["type"] == "login":
            massage = self.__login(require)
        print(massage)

    def __getRequire(self, msg):
        msg = self.cipher.decrypt(msg)
        type = msg.split("/")[0]
        username = msg.split(":")[1].split("?")[0]
        password = msg.split(":")[-1]
        return {
            "type": type,
            "username": username,
            "password": password
        }

    def __newUser(self, require):
        username = require["username"]
        password = require["password"]
        if not username and not password:
            return "请填写完整"
        try:
            # 将登录记录到数据库中
            conn, cur = getDB()
            cur.execute(add_user, (username, self.cipher.encrypt(password)))
            conn.commit()
            return "已注册用户"
        except:
            return "数据库出现问题"

    def __login(self, require):
        username = require["username"]
        password = require["password"]
        try:
            # 将登录记录到数据库中
            conn, cur = getDB()
            cur.execute(find_user, (username, self.cipher.encrypt(password)))
            user = cur.fetchone()
            if user:
                return "{}欢迎登录该系统".format(username)
            else:
                return "用户名or密码错误 & 未注册"
        except:
            return "数据库出现问题"

    def run_service(self) -> None:
        while True:
            recv_data = self.server.recvfrom(1024)
            msg = recv_data[0]
            self.__process(msg)


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
