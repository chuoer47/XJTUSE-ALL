import numpy as np
import matplotlib.pyplot as plt

# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

K1 = 4
K2 = 3
D = 10

# 定义时间范围
t1 = np.arange(0, 1, 0.01)
t2 = np.arange(1, 5, 0.01)

# 计算浓度
C0 = (K1*D)/(K1-K2)
C1 = C0 * (np.exp(-K2*t1)-np.exp(-K1*t1))
C2 = C0 * (np.exp(-K2*(t2-1))-np.exp(-K1*(t2-1))) + C0*(np.exp(-K2)-np.exp(-K1))*np.exp(-K2*(t2-1))

# 绘制图像
plt.figure()
plt.plot(t1, C1)
plt.plot(t2, C2)
plt.xlabel('时间')
plt.ylabel('浓度')
plt.title('药物浓度随时间的变化')
plt.show()