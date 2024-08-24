import os
import socket
import sys
import time

from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QDialog

import config
from lib.chatroom import Ui_SafeChatroom
from lib.cipher import AESCipher, RSCCipher


class ClientWindow(QDialog, Ui_SafeChatroom):
    # msg_recv 是存储客户端接收到的消息的存档
    msg_recv: str = ''
    # nickname 用于标识此客户端发送的消息
    now_nickname = 'unknown'
    # host 和 port 用于创建与聊天服务器之间的连接的套接字
    host: str
    port: int

    def __init__(self):
        """初始化 GUI、套接字、密钥对和客户端的工作线程"""
        super().__init__()
        self.setupUi(self)
        # 初始化Socket
        self.host = config.IP
        self.port = int(config.port)

        print('正在尝试连接服务器：{}:{}。'.format(self.host, self.port))
        try:
            self.connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connect.connect((self.host, self.port))
        except:
            print("第2次重试")
            try:
                self.connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.connect.connect((self.host, self.port))
            except:
                print('错误：根据 IP 地址和端口号找不到运行的服务器！')
                print('请检查设置或重新运行服务器。')
                sys.exit(-1)

        # 生成 RSC 密钥对
        print('找到服务器。正在生成 RSC 密钥对并交换密钥...')
        rsc = RSCCipher()
        try:
            # 将 RSC 公钥发送给服务器
            self.connect.send(rsc.pubKeyPEM)
            # 接收并解密 AES 密钥
            encrypted_AESkey = bytes(self.connect.recv(1024))
            self.AESkey = rsc.decrypt(encrypted_AESkey)
            print('接收到 AES 密钥：{}。'.format(self.AESkey))
        except:
            print('服务器已关闭。请尝试重新运行服务器。')
            sys.exit(-1)

        # 初始化线程
        print('正在启动线程...')
        self.recv_thread = RecvThread(self.connect, self.AESkey)
        self.recv_thread.trigger.connect(self.print_msg)
        self.recv_thread.start()

        # 绑定按钮
        self.send.clicked.connect(self.send_msg)
        self.nickname_changer.clicked.connect(self.change_nickname)
        self.historySaver.clicked.connect(self.save_history)
        print('所有准备工作完成。在 XJTU 聊天室 中尽情享受吧。')

    def send_msg(self) -> None:
        """'发送'按钮的功能，用于发送消息"""
        cipher = AESCipher(self.AESkey)
        msg = '<{}> : {}'.format(self.now_nickname, self.send_window.toPlainText())
        self.connect.send(cipher.encrypt(msg))
        # 清空
        self.send_window.clear()

    def print_msg(self, msg: str) -> None:
        """接收消息的线程函数"""
        # 鲁棒性
        if msg:
            # 将新接收到的消息添加到存档中
            self.msg_recv += msg + '\n'
            # 刷新消息浏览器
            self.recv_window.setText(self.msg_recv)

    def change_nickname(self) -> None:
        """更改当前客户端的昵称"""
        if not self.now_nickname == self.nickname.toPlainText():
            self.now_nickname = self.nickname.toPlainText()
            hint = '<System> 你的昵称已成功更改为 '
            self.print_msg(hint + self.now_nickname + '.')
        else:
            self.print_msg("你的昵称未改变")

    def save_history(self) -> None:
        """将聊天记录保存到 ./history 目录下的 .hs 文件中"""
        # 使用当前时间和 CPU 时间戳创建文件名
        t = time.localtime()
        tick = time.time()
        year, mon, day = t.tm_year, t.tm_mon, t.tm_mday
        fName = './history/' + str(year) + '.' + str(mon) + '.' + str(day) + '.' + str(tick) + '.hs'
        # 保存聊天记录
        if not os.path.exists('history'):
            os.makedirs('history')
        with open(fName, 'w') as fp:
            fp.write(self.msg_recv)
        hint = '<System> 当前聊天记录已成功存储到 ' + fName + ' 中'
        self.print_msg(hint)

    def recall(self) -> None:
        hint = '<System> 用户撤回了一条消息'
        pass


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

