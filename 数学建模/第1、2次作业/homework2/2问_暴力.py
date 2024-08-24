import numpy as np


def f(x):
    for i in range(1, 26):
        if (i * x) % 26 == 1:
            return i
    return 0


p_s = np.matrix([[4, 1], [5, 18]])
a_s = np.matrix([[7, 17], [15, 2]])
for x1 in range(0, 26):
    for x2 in range(0, 26):
        for x3 in range(0, 26):
            for x4 in range(0, 26):
                lst = [[x1, x2], [x3, x4]]
                a_s_I = (f(x1 * x4 - x2 * x3) * np.matrix(np.array(lst))) % 26
                A = (p_s * a_s_I) % 26
                very = (A * a_s) % 26
                flag = (very == p_s).all()
                if flag:
                    s = "goqbxcbuglosnfal"
                    s = np.array([(ord(i) - ord('a') + 1) % 26 for i in s]).reshape(8, 2).T
                    all = (A * s) % 26
                    all_lst = all.T.reshape(1, 16).tolist()[0]
                    res = ""
                    for i in all_lst:
                        res += chr(i + ord('a') - 1)
                    print(res)
