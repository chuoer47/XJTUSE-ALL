from config import *
from lab1.lab1 import TokenStream, Token, fileWriter


class BaseParser:
    """
    基础语法分析器类
    """
    flag: bool
    token: Token
    end: int

    def __init__(self, tokenStream, end=-1):
        self.tokenStream = tokenStream
        self.end = end
        self.get_next_token()
        self.err = ""

    def get_next_token(self):
        """
        获取下一个token
        """
        if self.end > 0:
            if self.tokenStream.index == self.end:
                self.token = Token('', 'FILE-END', 0)
                return
        self.token = self.tokenStream.getNextToken()

    def handle_syntax_error(self):
        """
        处理语法错误
        """
        self.flag = False
        print(f"第{self.tokenStream.index - 1}个词附近出现错误；")
        print(f"详细情况: 符号为{self.tokenStream.tokens[self.tokenStream.index - 1].lexeme} "
              f"类型为{self.tokenStream.tokens[self.tokenStream.index - 1].type}")
        self.get_next_token()

    def find(self, args):
        for i in range(self.tokenStream.index, len(self.tokenStream.tokens)):
            if self.tokenStream.tokens[i].code in args:
                return i
        return -1


class CAL_S(BaseParser):
    """
    算术表达式语法类
    算术表达式的语法如下:
    E->TE'
    E'->+TE'|-TE'|e
    T->FT'
    T'->*FT'|/FT'|e
    F->(E)|d
    """

    def start(self):
        """
        开始分析表达式
        """
        self.flag = True
        self.__E()
        return self.flag

    def __E(self):
        """
        处理E->TE'
        """
        self.__T()
        self.__E1()

    def __E1(self):
        """
        处理E'->+TE'|-TE'|e
        """
        if self.token.code in (PLUS, MINUS):
            self.get_next_token()
            self.__T()
            self.__E1()
        elif self.token.code not in (RPAREN, 0):
            self.handle_syntax_error()

    def __T(self):
        """
        处理T->FT'
        """
        self.__F()
        self.__T1()

    def __T1(self):
        """
        处理T'->*FT'|/FT'|e
        """
        if self.token.code in (MULTIPLY, DIVIDE):
            self.get_next_token()
            self.__F()
            self.__T1()
        elif self.token.code not in (MINUS, PLUS, RPAREN, 0):
            self.handle_syntax_error()

    def __F(self):
        """
        处理F->(E)|d
        """
        if self.token.code in (IDENTIFIER, CONSTANT):
            self.get_next_token()
        elif self.token.code == LPAREN:
            self.get_next_token()
            self.__E()
            if self.token.code == RPAREN:
                self.get_next_token()
            else:
                self.handle_syntax_error()
        else:
            self.handle_syntax_error()


class ASSIGN_S(BaseParser):
    """
    赋值语句表达类
    表达式如下形式
    IDENTIFIER ASSIGN 算术表达式
    """

    def start(self):
        self.flag = True

        # Check IDENTIFIER
        if self.token.code == IDENTIFIER:
            self.get_next_token()
        else:
            self.handle_syntax_error()
            return self.flag

        # Check ASSIGN
        if self.token.code == ASSIGN:
            cal = CAL_S(self.tokenStream, end=self.end)
            if not cal.start():
                self.handle_syntax_error()
                return self.flag
        else:
            self.handle_syntax_error()
            return self.flag

        return self.flag


class IF_S(BaseParser):
    """
    IF语句表达类
    按照实验报告的要求IF语句满足以下条件：
    1.无嵌套
    2.if 算术表达式 then 赋值语句 ;
    3.if 算术表达式 then 赋值语句 else 赋值语句;

    关键技术：
    我们使用了向前展望的方式来判断该文法是否满足条件，以此来进行判断，这不是一个很好的方法，
    但对于该特殊条件而言，该方法是有效而且快速的
    """

    def start(self):
        self.flag = True
        # 判断if
        if self.token.code != IF:
            self.handle_syntax_error()
            return self.flag

        # 判断算术表达式
        # 1.先找到THEN
        then_pivot = self.find((THEN,))
        # 2.然后判断算术表达式
        cal = CAL_S(self.tokenStream, then_pivot)
        flag = cal.start()
        if not flag:
            return False
        self.get_next_token()

        # 判断then
        if self.token.code != THEN:
            self.handle_syntax_error()
            return self.flag

        # 判断赋值语句
        # 1.先找到ELSE 或 ;
        pivot = self.find((ELSE, SEMICOLON))
        # 2.进行赋值表达式的判定
        assign = ASSIGN_S(self.tokenStream, pivot)
        flag = assign.start()
        if not flag:
            return False
        self.get_next_token()

        # 判断是否有else语句
        if self.token.code == ELSE:
            # 判断赋值语句
            # 1.先找到 ;
            pivot = self.find((SEMICOLON,))
            assign = ASSIGN_S(self.tokenStream, pivot)
            flag = assign.start()
            if not flag:
                return False
            self.get_next_token()

        # 判断结束
        if self.token.code != SEMICOLON:
            self.handle_syntax_error()
            return self.flag
        return self.flag


class WHILE_S(BaseParser):
    """
    WHILE语句表达类
    按照实验报告的要求IF语句满足以下条件：
    1.无嵌套
    2.while 算术表达式 DO 赋值语句 ;
    """

    def start(self):
        self.flag = True
        # 判断if
        if self.token.code != WHILE:
            self.handle_syntax_error()
            return self.flag

        # 判断算术表达式
        # 1.先找到DO
        then_pivot = self.find((DO,))
        # 2.然后判断算术表达式
        cal = CAL_S(self.tokenStream, then_pivot)
        flag = cal.start()
        if not flag:
            return False
        self.get_next_token()

        # 判断赋值语句
        # 1.先找到 ;
        pivot = self.find((SEMICOLON,))
        # 2.进行赋值表达式的判定
        assign = ASSIGN_S(self.tokenStream, pivot)
        flag = assign.start()
        if not flag:
            return False
        self.get_next_token()

        # 判断结束
        if self.token.code != SEMICOLON:
            self.handle_syntax_error()
            return self.flag
        return self.flag


class BEGIN:
    def __init__(self, tokenStream: TokenStream):
        self.ts = tokenStream

    def start(self):
        token = self.ts.getNowToken()

        if token.code == IF:
            ifs = IF_S(self.ts)
            return "IF分支语句，嵌套赋值语句" if ifs.start() else "语法错误:" + getErrorInfo(self.ts)

        if token.code == WHILE:
            ws = WHILE_S(self.ts)
            return "WHILE-DO循环语句，嵌套赋值语句" if ws.start() else "语法错误:" + getErrorInfo(self.ts)

        ass = ASSIGN_S(self.ts)
        return "赋值语句" if ass.start() else "语法错误:" + getErrorInfo(self.ts)


def getErrorInfo(tokenStream:TokenStream):
    err = (f"第{tokenStream.index - 1}个词附近出现错误；" + "\n"
           + f"详细情况: 符号为{tokenStream.tokens[tokenStream.index - 1].lexeme}"
           + f"类型为{tokenStream.tokens[tokenStream.index - 1].type}")
    return err


if __name__ == '__main__':
    fw = fileWriter("../fileSet/output/lab2.txt")
    cnt = 1
    with open('../fileSet/input/lab2.txt', 'r') as file:
        for content in file:
            ts = TokenStream(content)
            fw.write(f"第{cnt}行")
            fw.write(f"输入：{content.strip()}")
            fw.write(f"输出：")
            fw.write(str(ts).strip())
            parse = BEGIN(ts)
            fw.write(parse.start())
            fw.write("-----------------------------------------")
            cnt += 1
    print("完成！")
