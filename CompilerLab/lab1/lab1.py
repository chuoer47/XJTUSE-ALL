import re
from datetime import datetime

from config import *


class fileWriter:
    """封装文件输出类"""

    def __init__(self, filename):
        self.filename = filename
        # 初始化+清空+创建文件
        self.fw = open(self.filename, 'w', encoding="utf-8")
        self.fw.write(str(datetime.now()) + '\n')
        self.fw.close()

    def write(self, msg):
        # 追加模式
        self.fw = open(self.filename, 'a', encoding='utf-8')
        self.fw.write(msg + "\n")
        self.fw.close()


# Token class
class Token:
    def __init__(self, lexeme, type, code):
        self.lexeme = lexeme
        self.type = type
        self.code = code

    def __str__(self):
        return "{}\t{}\t{}".format(self.lexeme, self.type, self.code)


# TokenStream class
class TokenStream:
    def __init__(self, input_str):
        self.tokens = self.__tokenize(input_str)
        self.index = 0

    def __tokenize(self, input_str):
        # 正则表达式列表
        token_specification = [
            ('PROGRAM', r'program'),
            ('BEGIN', r'begin'),
            ('END', r'end'),
            ('VAR', r'var'),
            ('INTEGER', r'integer'),
            ('IF', r'if'),
            ('THEN', r'then'),
            ('ELSE', r'else'),
            ('DO', r'do'),
            ('WHILE', r'while'),
            ('IDENTIFIER', r'[a-zA-Z][a-zA-Z0-9]*'),
            ('CONSTANT', r'\d+'),
            ('PLUS', r'\+'),
            ('MINUS', r'-'),
            ('MULTIPLY', r'\*'),
            ('DIVIDE', r'/'),
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('ASSIGN', r'\:='),
            ('EQUAL', r'\='),
            ('GREATER_THAN', r'\>'),
            ('LESS_THAN', r'\<'),
            ('SEMICOLON', r'\;'),
            ('COMMA', r'\,'),
            ('COLON', r'\:'),
            ('SKIP', r'[ \t]+'),
            ('MISMATCH', r'.'),
        ]
        # 进行匹配
        token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
        tokens = []
        # 开始匹配
        for mo in re.finditer(token_regex, input_str):
            kind = mo.lastgroup
            value = mo.group()
            token_type = kind
            if kind in ['IDENTIFIER', 'CONSTANT']:
                token_type = kind
            if kind == 'SKIP':
                continue
            tokens.append(Token(value, token_type, code=identifiers[token_type]))

        return tokens

    def getNextToken(self):
        if self.index < len(self.tokens):
            token = self.tokens[self.index]
            self.index += 1
            return token
        else:
            return Token('', 'FILE-END', 0)

    def getNowToken(self):
        if self.index < len(self.tokens):
            token = self.tokens[self.index]
            return token
        else:
            return Token('', 'FILE-END', 0)

    def __str__(self):
        s = ""
        for token in self.tokens:
            s += "({}\t,{}\t,{})\n".format(token.lexeme, token.type, token.code)
        return s


if __name__ == '__main__':
    with open('../fileSet/input/lab1.txt', 'r') as file:
        content = file.read()
    ts = TokenStream(content)
    fw = fileWriter("../fileSet/output/lab1.txt")
    fw.write("(符号\t,识别符\t,识别码)")
    fw.write(str(ts))
    print("完成！")
