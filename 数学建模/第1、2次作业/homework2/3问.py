import numpy
import numpy as np

a = np.array([700, 300]).T
print("请输入A：")
A = float(input())
print("请输入B：")
B = float(input())
b = np.array(numpy.array([[1 - A, B],
                          [A, 1 - B]]))
while True:
    t = b.dot(a)
    if ((t - a) <= 1e-5).all():
        break
    a = t
    print(a)
