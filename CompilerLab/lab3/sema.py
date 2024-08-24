#!/usr/bin/env python
# -*- coding: utf-8 -*-
import lexer
from lab1.lab1 import fileWriter

from util import Production, Symbol, Entry


TERMINAL_SET = set()

NON_TERMINAL_SET = set()

SYMBOL_DICT = {}

PRODUCTION_LIST = []

PARSING_TABLE = {}

SEMA_ACTION_TABLE = {}

SYMBOL_STACK = []

SYMBOL_TABLE = []

LAST_STACK_TOP_SYMBOL = None

CODE_SIZE = 0

CODE_RESULT = []

current_symbol_table_pos = 0
current_symbol_index = 0

CURRENT_CONDITION_NODE = None


def P11():
    """
    将LAST_STACK_TOP_SYMBOL所代表的符号的父节点的属性"type"设置为"int"，"length"设置为4。
    这是用于声明一个整型变量。
    """
    symbol_for_str(LAST_STACK_TOP_SYMBOL).father.attr["type"] = "int"
    symbol_for_str(LAST_STACK_TOP_SYMBOL).father.attr["length"] = 4


def P12():
    """
    将LAST_STACK_TOP_SYMBOL所代表的符号的父节点的属性"type"设置为"float"，"length"设置为4。
    这是用于声明一个浮点型变量。
    """
    symbol_for_str(LAST_STACK_TOP_SYMBOL).father.attr["type"] = "float"
    symbol_for_str(LAST_STACK_TOP_SYMBOL).father.attr["length"] = 4


def P13():
    """
    将LAST_STACK_TOP_SYMBOL所代表的符号的父节点的属性"type"设置为"double"，"length"设置为8。
    这是用于声明一个双精度浮点型变量。
    """
    symbol_for_str(LAST_STACK_TOP_SYMBOL).father.attr["type"] = "double"
    symbol_for_str(LAST_STACK_TOP_SYMBOL).father.attr["length"] = 8


def P14():
    """
    将LAST_STACK_TOP_SYMBOL所代表的符号的父节点的属性"type"设置为"short"，"length"设置为2。
    这是用于声明一个短整型变量。
    """
    symbol_for_str(LAST_STACK_TOP_SYMBOL).father.attr["type"] = "short"
    symbol_for_str(LAST_STACK_TOP_SYMBOL).father.attr["length"] = 2


def P15():
    """
    将LAST_STACK_TOP_SYMBOL所代表的符号的父节点的属性"type"设置为"long"，"length"设置为4。
    这是用于声明一个长整型变量。
    """
    symbol_for_str(LAST_STACK_TOP_SYMBOL).father.attr["type"] = "long"
    symbol_for_str(LAST_STACK_TOP_SYMBOL).father.attr["length"] = 4


def P21():
    """
    将LAST_STACK_TOP_SYMBOL所代表的符号的父节点的属性"type"和"length"设置为其第一个子节点的相应属性。
    这是用于声明一个数组或结构体成员。
    """
    symbol_for_str(LAST_STACK_TOP_SYMBOL).father.attr["type"] = (
        symbol_for_str(LAST_STACK_TOP_SYMBOL).father.children[0].attr["type"]
    )
    symbol_for_str(LAST_STACK_TOP_SYMBOL).father.attr["length"] = (
        symbol_for_str(LAST_STACK_TOP_SYMBOL).father.children[0].attr["length"]
    )


def P22():
    """
    将LAST_STACK_TOP_SYMBOL所代表的符号的第一个子节点的相关信息添加到符号表中。
    更新当前符号表位置和索引。
    这是用于添加一个新的变量声明到符号表中。
    """
    global current_symbol_table_pos
    global current_symbol_index
    s = symbol_for_str(LAST_STACK_TOP_SYMBOL).father.children[0]
    SYMBOL_TABLE.append(Entry(s.attr["type"], s.attr["length"], s.attr["name"]))
    current_symbol_index += 1
    current_symbol_table_pos += s.attr["length"]


def P31():
    """
    将LAST_STACK_TOP_SYMBOL所代表的符号的父节点的属性"name"设置为其第二个子节点的词法值。
    这是用于设置一个变量或函数的名称。
    """
    f = symbol_for_str(LAST_STACK_TOP_SYMBOL).father
    f.attr["name"] = f.children[1].lexical_value


def P41():
    """
    将LAST_STACK_TOP_SYMBOL所代表的符号的父节点的属性"type"设置为"int"，"value"设置为其第一个子节点的词法值。
    这是用于给一个整型变量赋值。
    """
    f = symbol_for_str(LAST_STACK_TOP_SYMBOL).father
    f.attr["type"] = "int"
    f.attr["value"] = f.children[0].lexical_value


def P42():
    """
    将LAST_STACK_TOP_SYMBOL所代表的符号的父节点的属性"type"设置为"float"，"value"设置为其第一个子节点的词法值转换为float。
    这是用于给一个浮点型变量赋值。
    """
    f = symbol_for_str(LAST_STACK_TOP_SYMBOL).father
    f.attr["type"] = "float"
    f.attr["value"] = float(f.children[0].lexical_value)


def P43():
    """
    将LAST_STACK_TOP_SYMBOL所代表的符号的父节点的属性"type"设置为"short"，"value"设置为其第一个子节点的词法值。
    这是用于给一个短整型变量赋值。
    """
    f = symbol_for_str(LAST_STACK_TOP_SYMBOL).father
    f.attr["type"] = "short"
    f.attr["value"] = f.children[0].lexical_value


def P44():
    """
    将LAST_STACK_TOP_SYMBOL所代表的符号的父节点的属性"type"设置为"long"，"value"设置为其第一个子节点的词法值。
    这是用于给一个长整型变量赋值。
    """
    f = symbol_for_str(LAST_STACK_TOP_SYMBOL).father
    f.attr["type"] = "long"
    f.attr["value"] = f.children[0].lexical_value


def P51():
    """
    没有任何操作。
    """
    pass


def P52():
    """
    将LAST_STACK_TOP_SYMBOL所代表的符号的父节点的父节点的属性"type"和"value"设置为其第一个子节点的相应属性。
    这是用于给一个复合类型变量(如数组或结构体)的成员赋值。
    """
    f = symbol_for_str(LAST_STACK_TOP_SYMBOL).father.father
    f.attr["type"] = f.children[0].attr["type"]
    f.attr["value"] = f.children[0].attr["value"]


def P61():
    """
    处理表达式求值
    1. 获取表达式的父节点
    2. 如果父节点的子节点少于3个,则继续向上找父节点
    3. 获取表达式左右操作数和运算符节点
    4. 检查左操作数是否定义,如果未定义则报语法错误
    5. 检查左右操作数类型是否匹配,如果不匹配则报语法错误
    6. 根据运算符和因子计算表达式结果
    7. 将结果赋值给左操作数
    """
    f = symbol_for_str(LAST_STACK_TOP_SYMBOL).father
    if len(f.children) < 3:
        f = f.father.father.father.father

    l = f.children[0]
    r = f.children[2]

    fac = f.children[4]

    lv = search_for_symbol(l.lexical_value)
    if lv is None:
        syntax_error("undefined " + l.lexical_value)
        return

    if lv.type != r.attr["type"]:
        syntax_error("type mismatch")
        return

    result = None
    if "op" in fac.attr:
        if fac.attr["op"] == "+":
            result = f.attr["value"] + fac.attr["factor"]

        if fac.attr["op"] == "*":
            result = f.attr["value"] * fac.attr["factor"]
    else:
        result = r.attr["value"]
    fac.attr = {}

    code_output(lv.name + " := " + str(result))


def P62():
    """
    处理赋值语句
    将右操作数的类型和值赋给左操作数
    """
    f = symbol_for_str(LAST_STACK_TOP_SYMBOL).father.father.father.father
    f.attr["type"] = f.children[2].attr["type"]
    f.attr["value"] = f.children[2].attr["value"]


def P71():
    """
    处理 GOTO 语句
    将左操作数的类型和值赋给目标位置
    """
    f = symbol_for_str(LAST_STACK_TOP_SYMBOL).father.father.father
    f.attr["type"] = f.children[0].attr["type"]
    f.attr["value"] = f.children[0].attr["value"]


def P72():
    """
    处理 GOTO 语句,将左操作数的值加1
    """
    f = symbol_for_str(LAST_STACK_TOP_SYMBOL).father.father.father
    f.attr["type"] = f.children[0].attr["type"]
    f.attr["value"] = f.children[0].attr["value"] + 1


def P73():
    """
    处理 GOTO 语句,将左操作数的值减1
    """
    f = symbol_for_str(LAST_STACK_TOP_SYMBOL).father.father.father
    f.attr["type"] = f.children[0].attr["type"]
    f.attr["value"] = f.children[0].attr["value"] - 1


def P81():
    """
    处理 IF 语句
    1. 获取条件表达式节点
    2. 生成 IF 语句的代码
    3. 保存条件表达式节点的位置信息
    """
    global CURRENT_CONDITION_NODE
    f = symbol_for_str(LAST_STACK_TOP_SYMBOL).father
    CURRENT_CONDITION_NODE = f
    e = f.children[2]
    code_output("IF " + str(e.attr["value"]) + " GOTO " + str(CODE_SIZE + 2))
    code_output(None)
    f.attr["back"] = CODE_SIZE - 1


def P82():
    """
    处理 IF 语句,修改跳转语句为跳转到当前位置
    """
    prev = CURRENT_CONDITION_NODE.attr["back"]
    CODE_RESULT[prev] = "GOTO " + str(CODE_SIZE)


def P91():
    """
    处理 WHILE 语句
    1. 获取条件表达式节点
    2. 生成 IF 语句的代码
    3. 保存条件表达式节点的位置信息
    """
    global CURRENT_CONDITION_NODE
    f = symbol_for_str(LAST_STACK_TOP_SYMBOL).father
    CURRENT_CONDITION_NODE = f
    e = f.children[2]
    code_output("IF " + str(e.attr["value"]) + " GOTO " + str(CODE_SIZE + 2))
    code_output(None)
    f.attr["back"] = CODE_SIZE - 1


def P92():
    """
    处理 WHILE 语句,修改跳转语句为跳转到条件判断位置
    """
    prev = CURRENT_CONDITION_NODE.attr["back"]
    CODE_RESULT[prev] = "GOTO " + str(CODE_SIZE + 1)
    code_output("GOTO " + str(prev - 1))


def P101():
    """
    处理表达式中的运算符和因子
    将运算符和因子保存到表达式节点的属性中
    """
    f = symbol_for_str(LAST_STACK_TOP_SYMBOL).father.father.father.father
    f.attr["op"] = f.children[0].lexical_value
    f.attr["factor"] = f.children[1].attr["value"]


def P102():
    """
    处理表达式中的运算符和因子
    将运算符和因子保存到表达式节点的属性中
    """
    f = symbol_for_str(LAST_STACK_TOP_SYMBOL).father.father.father.father
    f.attr["op"] = f.children[0].lexical_value
    f.attr["factor"] = f.children[1].attr["value"]


def no_action():
    pass


SEMA_ACTION_TABLE["P11"] = P11
SEMA_ACTION_TABLE["P12"] = P12
SEMA_ACTION_TABLE["P13"] = P13
SEMA_ACTION_TABLE["P14"] = P14
SEMA_ACTION_TABLE["P15"] = P15
SEMA_ACTION_TABLE["P21"] = P21
SEMA_ACTION_TABLE["P22"] = P22
SEMA_ACTION_TABLE["P31"] = P31
SEMA_ACTION_TABLE["P41"] = P41
SEMA_ACTION_TABLE["P42"] = P42
SEMA_ACTION_TABLE["P43"] = P43
SEMA_ACTION_TABLE["P44"] = P44
SEMA_ACTION_TABLE["P51"] = P51
SEMA_ACTION_TABLE["P52"] = P52
SEMA_ACTION_TABLE["P61"] = P61
SEMA_ACTION_TABLE["P62"] = P62
SEMA_ACTION_TABLE["P71"] = P71
SEMA_ACTION_TABLE["P72"] = P72
SEMA_ACTION_TABLE["P73"] = P73
SEMA_ACTION_TABLE["P81"] = P81
SEMA_ACTION_TABLE["P82"] = P82
SEMA_ACTION_TABLE["P91"] = P91
SEMA_ACTION_TABLE["P92"] = P92
SEMA_ACTION_TABLE["P101"] = P101
SEMA_ACTION_TABLE["P102"] = P102

SEMA_ACTION_TABLE["null"] = no_action


def symbol_for_str(string):
    return SYMBOL_DICT[string]


def is_terminal(string):
    return string in TERMINAL_SET


def syntax_error(msg, line=None, row=None):
    if line is None:
        line = lexer.current_line + 1
    if row is None:
        row = lexer.current_row + 1
    print(str(line) + ":" + str(row) + " Syntax error: " + msg)


def code_output(code):
    global CODE_SIZE
    CODE_SIZE += 1
    CODE_RESULT.append(code)


def search_for_symbol(name):
    for e in SYMBOL_TABLE:
        if e.name == name:
            return e


def prepare_symbols_and_productions():
    f = open("dataset/grammer.txt", "r")
    lines = f.readlines()
    terminal = False
    production = False
    for l in lines:
        if l.strip() == "*terminals":
            terminal = True
            production = False
            continue
        if l.strip() == "*productions":
            terminal = False
            production = True
            continue
        if l.strip() == "*end":
            break
        if terminal:
            TERMINAL_SET.update([l.strip()])
        if production:
            left = l.split("::=")[0].strip()
            NON_TERMINAL_SET.update([left])

            try:
                right = l.split("::=")[1].strip()
                if right == "":
                    raise IndexError
                p = Production(left, right.split(" "))
            except IndexError:
                p = Production(left, ["null"])

            PRODUCTION_LIST.append(p)

    for s in TERMINAL_SET:
        sym = Symbol(s, sym_type="T")
        SYMBOL_DICT[s] = sym

    for s in NON_TERMINAL_SET:
        sym = Symbol(s, sym_type="N")
        SYMBOL_DICT[s] = sym


def get_nullable():
    """
    Calculate and mark non-terminals found that is nullable(can derive null).
    We do this first, so we can use the result when calculating First and Follow.
    """
    changes = True
    while changes:
        changes = False
        for p in PRODUCTION_LIST:
            if not symbol_for_str(p.left).is_nullable:
                if p.right[0] == "null":
                    symbol_for_str(p.left).is_nullable = True
                    changes = True
                    continue
                else:
                    right_is_nullable = symbol_for_str(p.right[0]).is_nullable
                    # For X -> Y1 ... YN, Nullable(X) = Nullable(Y1) &
                    # Nullable(Y2) ... & Nullable(YN)
                    for r in p.right[1:]:
                        if r.startswith("P"):
                            continue
                        right_is_nullable = (
                            right_is_nullable & symbol_for_str(r).is_nullable
                        )

                    if right_is_nullable:
                        changes = True
                        symbol_for_str(p.left).is_nullable = True


def get_first():
    """
    计算每个符号的 First 集合。
    """
    # 初始化终结符的 First 集合
    for s in TERMINAL_SET:
        sym = SYMBOL_DICT[s]
        sym.first_set = set([s])

    # 初始化非终结符的 First 集合
    for s in NON_TERMINAL_SET:
        sym = SYMBOL_DICT[s]
        if sym.is_nullable:
            sym.first_set = set(["null"])
        else:
            sym.first_set = set()

    # 迭代计算 First 集合直到稳定
    while True:
        first_set_is_stable = True
        for p in PRODUCTION_LIST:
            sym_left = symbol_for_str(p.left)
            if p.right[0] == "null":
                sym_left.first_set.update(set(["null"]))
                continue
            previous_first_set = set(sym_left.first_set)

            for s in p.right:
                # 对于 X -> Y..., First(X) = First(X) U First(Y)
                sym_right = symbol_for_str(s)
                sym_left.first_set.update(sym_right.first_set)
                # 对于 X -> Y1 Y2 ... Yi-1 , 如果 Y1...Yi-1 都是可空的
                # 则 First(X) = First(X) U First(Y1) U First(Y2) ...
                if sym_right.is_nullable:
                    continue
                else:
                    break

            if previous_first_set != sym_left.first_set:
                first_set_is_stable = False

        if first_set_is_stable:
            break


def get_follow():
    """
    计算每个非终结符的 Follow 集合。
    """
    # 初始化每个非终结符的 Follow 集合
    for s in NON_TERMINAL_SET:
        sym = symbol_for_str(s)
        sym.follow_set = set()

    # 初始化开始符号的 Follow 集合
    symbol_for_str("<s>").follow_set.update(set(["#"]))

    # 迭代计算 Follow 集合直到稳定
    while True:
        follow_set_is_stable = True
        for p in PRODUCTION_LIST:
            sym_left = symbol_for_str(p.left)
            if sym_left.is_terminal():
                continue
            for i, s in enumerate(p.right):
                if s == "null":
                    continue
                if s.startswith("P"):
                    continue
                if symbol_for_str(s).is_terminal():
                    continue
                current_symbol = symbol_for_str(s)
                previous_follow_set = set(current_symbol.follow_set)
                next_is_nullable = True
                for s2 in p.right[i + 1:]:
                    if s2.startswith("P"):
                        continue
                    # 对于 X -> sYt, Follow(Y) = Follow(Y) U First(t)
                    next_symbol = symbol_for_str(s2)
                    current_symbol.follow_set.update(next_symbol.first_set)
                    if next_symbol.is_nullable:
                        continue
                    else:
                        next_is_nullable = False
                        break
                if next_is_nullable:
                    # 对于 X -> sYt, 如果 t 是可空的,
                    # Follow(Y) = Follow(Y) U Follow(X)
                    current_symbol.follow_set.update(sym_left.follow_set)

                if current_symbol.follow_set != previous_follow_set:
                    follow_set_is_stable = False

        if follow_set_is_stable:
            break


def get_select():
    """
    Calculate Select set for each production.
    """
    while True:
        select_set_is_stable = True
        for p in PRODUCTION_LIST:
            sym_left = symbol_for_str(p.left)
            previous_select = set(p.select)
            if p.right[0] == "null":
                # For A -> a, if a is null, Select(i) = Follow(A)
                p.select.update(sym_left.follow_set)
                continue
            sym_right = symbol_for_str(p.right[0])
            # Otherwise, Select(i) = First(a)
            p.select.update(sym_right.first_set)
            # If a is nullable, Select(i) = First(a) U Follow(A)
            if sym_right.is_nullable:
                p.select.update(sym_right.first_set.union(sym_left.follow_set))
            if previous_select != p.select:
                select_set_is_stable = False
        if select_set_is_stable:
            break


def get_parsing_table():
    """
    Calculate parsing table.
    """
    global PARSING_TABLE
    for non_terminal in NON_TERMINAL_SET:
        if non_terminal.startswith("P"):
            continue
        PARSING_TABLE[non_terminal] = {}
        for p in PRODUCTION_LIST:
            if non_terminal == p.left:
                for symbol in p.select:
                    PARSING_TABLE[non_terminal][symbol] = p
        # Calculate SYNC
        for symbol in symbol_for_str(non_terminal).follow_set:
            if is_terminal(symbol):
                try:
                    p = PARSING_TABLE[non_terminal][symbol]
                except KeyError:
                    PARSING_TABLE[non_terminal][symbol] = "SYNC"

        for symbol in symbol_for_str(non_terminal).first_set:
            if is_terminal(symbol):
                try:
                    p = PARSING_TABLE[non_terminal][symbol]
                except KeyError:
                    PARSING_TABLE[non_terminal][symbol] = "SYNC"

                    # prettyprint_parsing_table()


def prettyprint_parsing_table():
    for non_terminal in PARSING_TABLE.keys():
        symbol_to_production_list = []
        for symbol in PARSING_TABLE[non_terminal]:
            p = PARSING_TABLE[non_terminal][symbol]
            symbol_to_production = str(symbol) + ":" + str(p)
            symbol_to_production_list.append(symbol_to_production)

        print(non_terminal)
        print(symbol_to_production_list)


def print_symbol_table():
    res = ""
    for t in SYMBOL_TABLE:
        res += str(t)+"\n"
        print(t)
    return res


def print_code_result():
    res = ""
    for r in CODE_RESULT:
        res += str(str(CODE_RESULT.index(r)) + ": " + str(r))+"\n"
        print(str(CODE_RESULT.index(r)) + ": " + r)
    return res

def next_token():
    r = lexer.scanner()
    while r is None:
        r = lexer.scanner()
    return r


def prepare_grammar():
    prepare_symbols_and_productions()
    get_nullable()
    get_first()
    get_follow()
    get_select()
    get_parsing_table()


def do_sema_actions(symbol):
    SEMA_ACTION_TABLE[symbol]()


def do_parsing():
    global LAST_STACK_TOP_SYMBOL
    SYMBOL_STACK.append("#")
    SYMBOL_STACK.append("<s>")

    token_tuple = next_token()
    productions = open("productions.txt", "w")
    stack = open("stack.txt", "w")
    while len(SYMBOL_STACK) > 0:
        stack_top_symbol = SYMBOL_STACK[-1]
        while stack_top_symbol == "null":
            SYMBOL_STACK.pop()
            stack_top_symbol = SYMBOL_STACK[-1]

        if stack_top_symbol.startswith("P"):
            do_sema_actions(stack_top_symbol)
            SYMBOL_STACK.pop()
            stack.write(str(SYMBOL_STACK) + "\n")
            continue
        current_token = token_tuple[0]
        if current_token == "OP" or current_token == "SEP":
            current_token = token_tuple[1]

        if current_token == "SCANEOF":
            current_token = "#"

        if stack_top_symbol == "null":
            LAST_STACK_TOP_SYMBOL = SYMBOL_STACK.pop()
            continue

        if stack_top_symbol == "#":
            break

        if not is_terminal(stack_top_symbol):
            try:
                p = PARSING_TABLE[stack_top_symbol][current_token]
            except KeyError:
                # Stack top symbol unmatched, ignore it
                syntax_error("unmatched")
                token_tuple = next_token()
                continue

            if p == "SYNC":
                # SYNC recognized, pop Stack
                syntax_error("sync symbol, recovering")
                LAST_STACK_TOP_SYMBOL = SYMBOL_STACK.pop()
                stack.write(str(SYMBOL_STACK) + "\n")
                productions.write(str(p) + "\n")
                continue

            stack.write(str(SYMBOL_STACK) + "\n")
            productions.write(str(p) + "\n")
            LAST_STACK_TOP_SYMBOL = SYMBOL_STACK.pop()
            SYMBOL_STACK.extend(reversed(p.right))
            symbol_for_str((LAST_STACK_TOP_SYMBOL)).children = []
            for symbol in p.right:
                if symbol.startswith("P"):
                    symbol_for_str(LAST_STACK_TOP_SYMBOL).children.append(symbol)
                    continue

                if symbol == "null":
                    continue
                t = symbol_for_str(symbol)
                symbol_for_str(LAST_STACK_TOP_SYMBOL).children.append(t)
                t.father = symbol_for_str(LAST_STACK_TOP_SYMBOL)

        else:
            symbol_for_str(stack_top_symbol).lexical_value = token_tuple[1]
            LAST_STACK_TOP_SYMBOL = SYMBOL_STACK.pop()
            stack.write(str(SYMBOL_STACK) + "\n")
            token_tuple = next_token()

    productions.close()
    stack.close()


def main():
    fw = fileWriter("dataset/output.txt")
    prepare_grammar()
    lexer.read_source_file("dataset/input.txt")
    do_parsing()
    fw.write("符号表：")
    fw.write("------------")
    fw.write(print_symbol_table())
    fw.write("中间代码：")
    fw.write("------------")
    fw.write(print_code_result())


if __name__ == "__main__":
    main()
