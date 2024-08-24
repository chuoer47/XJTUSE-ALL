import socket
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QDialog

import config
from lib.TCP import Ui_TCP
from lib.cipher import AESCipher, RSCCipher
from network_lab.UDP.UDPconfig import AESkey


class ClientWindow(QDialog, Ui_TCP):
    # msg_recv 是存储客户端接收到的消息的存档
    msg_recv: str = ''
    # nickname 用于标识此客户端发送的消息
    now_nickname = 'unknown'
    # host 和 port 用于创建与聊天服务器之间的连接的套接字
    host: str
    port: int
    cipher: AESCipher

    def __init__(self):
        """初始化 GUI、套接字、密钥对和客户端的工作线程"""
        super().__init__()
        self.setupUi(self)
        # 初始化 UDP Socket 用来发送消息
        self.host = config.IP
        self.port = int(config.port)
        self.address = (self.host, self.port)
        self.connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # 获得AES加密
        self.AESkey = AESkey
        self.cipher = AESCipher(self.AESkey)

        # 初始化 UDP Socket 用来接收消息


        # 绑定按钮
        self.newUser.clicked.connect(self.__newUser)
        self.login.clicked.connect(self.__login)
        print('所有准备工作完成。')

    def __send(self, msg):
        self.connect.sendto(msg, self.address)

    def __newUser(self) -> None:
        username = self.username.text()
        password = self.password.text()
        msg = "newUser/username:{}?password:{}".format(username, password)
        self.__send(self.cipher.encrypt(msg))
        print("已经发送注册请求")

    def __login(self) -> None:
        username = self.username.text()
        password = self.password.text()
        msg = "login/username:{}?password:{}".format(username, password)
        self.__send(self.cipher.encrypt(msg))
        print("已经发送登录请求")



class RecvThread(QThread):
    """用于从服务器接收消息的线程"""
    # 信号
    trigger = pyqtSignal(str)
    msg_recv: str

    def __init__(self, connect: socket.socket, AES_key):
        super(RecvThread, self).__init__()
        self.connect = connect
        self.cipher = AESCipher(AES_key)

    # 重写线程的 run() 方法
    def run(self):
        buffer_size = 1024  # 缓冲区大小，用于一次性接收更多的数据
        msg: str  # 用于存储接收到的数据的缓冲区
        # 分块，利用缓存区读取任意长的文本
        while True:
            msg = self.cipher.decrypt(self.connect.recv(buffer_size))
            # 解密接收到的消息并发送到槽函数
            if msg:
                self.trigger.emit(msg)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    client = ClientWindow()
    client.show()
    sys.exit(app.exec())
