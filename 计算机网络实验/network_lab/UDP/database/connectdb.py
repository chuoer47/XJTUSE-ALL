import sqlite3

from xjtu_anonymous_chatroom.database.config import database_path


def getDB():
    conn = sqlite3.connect(database_path)
    # 创建一个游标 cursor
    cur = conn.cursor()
    return conn, cur
