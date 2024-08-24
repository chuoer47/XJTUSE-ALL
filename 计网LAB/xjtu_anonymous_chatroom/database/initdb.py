"""初始化文件"""
from xjtu_anonymous_chatroom.database.connectdb import getDB

def initdb(conn, cur):
    """删除所有表格"""
    # 查询所有表的名称
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    # 删除每个表
    for table in tables:
        table_name = table[0]
        try:
            cur.execute(f"DROP TABLE {table_name};")
        except:
            continue
    # 提交更改并关闭连接
    conn.commit()

    """创建新的表格"""
    # 建表的sql语句
    creat_comer_record = '''CREATE TABLE comer_record
                   (id INTEGER PRIMARY KEY,
                   requester TEXT,
                    responder TEXT,
                    start_time TEXT,
                    end_time TEXT);'''

    # 执行sql语句
    cur.execute(creat_comer_record)

    # 创建表的 SQL 语句
    create_chat_logs = '''
        CREATE TABLE IF NOT EXISTS chat_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(255) NOT NULL,
            message TEXT NOT NULL,
        message_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        '''

    # 执行创建表的 SQL 语句
    cur.execute(create_chat_logs)

    # 连接完数据库并不会自动提交，所以需要手动 commit 你的改动conn.commit()
    # 提交改动的方法
    conn.commit()


if __name__ == '__main__':
    conn, cur = getDB()
    initdb(conn, cur)
