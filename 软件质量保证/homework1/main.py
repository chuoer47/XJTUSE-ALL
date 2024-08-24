import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import itertools

# 定义a、b、c的取值范围
lst = [1, 2, 49, 50, 51, 99, 100]
a_values = lst
b_values = lst
c_values = lst

# 获取笛卡尔乘积的点
points = list(itertools.product(a_values, b_values, c_values))

# 初始化绘图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制点
for point in points:
    ax.scatter(point[0], point[1], point[2], c='r', marker='o')

# 设置坐标轴标签
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('c')

# 显示图形
plt.show()