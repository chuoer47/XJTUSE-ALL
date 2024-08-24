import numpy as np


def str2num(s):
    return ord(s) - ord('a') + 1


def num2str(n):
    return chr(n + ord('a') - 1)


def inv(x):
    """
    :param x: 特征值
    :return: 特征值的逆
    """
    x = int(x + 0.5)  # 浮点数和整数的精度问题
    for i in range(1, 26):
        if (i * x) % 26 == 1:
            return i
    return 0


print("输入你需要加密的信息：")
# s = input().strip()
s = "meet"
if len(s) % 2 == 1:
    s += "a"  # 自动补全一下,方便后续操作，自己理解的时候，注意一下即可
A = np.array([[1, 2],
              [0, 5]], dtype=np.int32)
B = np.array([str2num(i) for i in s]).reshape(2, len(s) // 2)
C = A.dot(B) % 26  # 加密

output = [num2str(i) for i in np.nditer(C)]
print("加密后的数据为：", *output)

# 下面给一个简单的模26矩阵的变换操作求逆矩阵:
AI = (inv(np.linalg.det(A)) * (np.linalg.inv(A) * np.linalg.det(A))) % 26  # 得到逆矩阵
RA = AI.dot(C) % 26
origin = [num2str(int(i + 0.5)) for i in np.nditer(RA)]
print("解密后的数据为：", *origin)
