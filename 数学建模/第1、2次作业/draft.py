import numpy as np


def f(x):
    for i in range(1, 26):
        if (i * x) % 26 == 1:
            return i


A = np.matrix([[4, 1], [5, 18]])
B = np.matrix([[7, 17], [15, 2]])
B_I = (f(7 * 2 - 15 * 17) * np.matrix([[2, -17], [-15, 7]])) % 26
C = (A * B_I) % 26  # 获得破译矩阵
print(C)
# 下面为破译所有信息操作：
s = "goqbxcbuglosnfal"
s = np.array([(ord(i) - ord('a') + 1) % 26 for i in s]).reshape(8, 2).T
S = (C * s) % 26
# 直接转化为列表操作
S_lst = S.T.reshape(1, 16).tolist()[0]
res = ""
for i in S_lst:
    res += chr(i + ord('a') - 1)
print(res)
