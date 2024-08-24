# Token types
IDENTIFIER, CONSTANT, PROGRAM, BEGIN, END, VAR, INTEGER, IF, THEN, ELSE, DO, WHILE = range(1, 13)
PLUS, MINUS, MULTIPLY, DIVIDE = 14, 15, 16, 17
LPAREN, RPAREN = 18, 19
EQUAL, GREATER_THAN, LESS_THAN = 20, 21, 22
SEMICOLON, COMMA, COLON, ASSIGN = 23, 24, 25, 26
ERROR = -1

identifiers = {
    'IDENTIFIER': 1,
    'CONSTANT': 2,
    'PROGRAM': 3,
    'BEGIN': 4,
    'END': 5,
    'VAR': 6,
    'INTEGER': 7,
    'IF': 8,
    'THEN': 9,
    'ELSE': 10,
    'DO': 11,
    'WHILE': 12,
    'PLUS': 14,
    'MINUS': 15,
    'MULTIPLY': 16,
    'DIVIDE': 17,
    'LPAREN': 18,
    'RPAREN': 19,
    'EQUAL': 20,
    'GREATER_THAN': 21,
    'LESS_THAN': 22,
    'SEMICOLON': 23,
    'COMMA': 24,
    'COLON': 25,
    'ASSIGN': 26,
    'ERROR': -1
}


re_identifiers = {
    1: 'IDENTIFIER',
    2: 'CONSTANT',
    3: 'PROGRAM',
    4: 'BEGIN',
    5: 'END',
    6: 'VAR',
    7: 'INTEGER',
    8: 'IF',
    9: 'THEN',
    10: 'ELSE',
    11: 'DO',
    12: 'WHILE',
    14: 'PLUS',
    15: 'MINUS',
    16: 'MULTIPLY',
    17: 'DIVIDE',
    18: 'LPAREN',
    19: 'RPAREN',
    20: 'EQUAL',
    21: 'GREATER_THAN',
    22: 'LESS_THAN',
    23: 'SEMICOLON',
    24: 'COMMA',
    25: 'COLON',
    26: 'ASSIGN',
    -1: 'ERROR'
}
