import numpy as np


def f(x):
    for i in range(1, 26):
        if (i * x) % 26 == 1:
            return i


A = np.array([[4, 1], [5, 18]])
B = np.array([[7, 17], [15, 2]])
B_I = (f(7 * 2 - 15 * 17) * np.array([[2, -17], [-15, 7]])) % 26
C = (A.dot(B_I)) % 26  # 获得破译矩阵

# 下面为破译所有信息操作：
s = "goqbxcbuglosnfal"
s = np.array([(ord(i) - ord('a') + 1) % 26 for i in s]).reshape(8, 2).T
S = (C.dot(s)) % 26

# 直接转化为列表操作,复原字符串
S_lst = S.T.reshape(1, 16).tolist()[0]
res = ""
for i in S_lst:
    res += chr(i + ord('a') - 1)
print(res)
