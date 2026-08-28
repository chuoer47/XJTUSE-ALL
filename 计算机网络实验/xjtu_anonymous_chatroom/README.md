# XJTUer 网络聊天室
这是一个XJTUer的匿名聊天室，主要技术栈为PyQt5,Sqlite3,Socket编程和RSA，AES密码学知识。
> 实验报告可以见:https://ecemf3mg97.feishu.cn/docx/JqN5dARHWoowufxGS4zcZ7XHnCf

## 项目
### 项目构成

项目主要由chatRoom工作包和database数据库组成。

1. client文件夹:包含了client（客户端代码以及配置）
2. server文件夹:包含了server（服务器代码以及配置）
3. database:一些sqlite数据库的表和初始化，预置SQL语句

### 项目启动

1. server启动：

```python
python ./chatRoom/server/server.py
```

2. client启动(可以生成多个):

```python
python ./chatRoom/client/client.py
```

### 项目注意事项
1. 我通过线程给server内置了一些命令（直接输入即可），当server启动后，有exit和reboot命令
   
   - exit:退出程序
   - reboot:清空数据库，但不退出程序

2. 项目可能需要需要配置`database/config.py`中的路径，因为系统不一样导致的。
3. 注意server只能启用一个，而client可以启动多个
4. 改TCP链接的端口，可以在对应的config.py配置文件进行修改，注意：一定要匹配上！
5. 数据库有时候会出错，没找到为什么会出这样的bug....

# 致谢
感谢 https://github.com/debidong/SafeChatroom ，不过由于我魔改了较多，所以没办法提交PR了