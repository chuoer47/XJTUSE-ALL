import numpy as np
from matplotlib import pyplot as plt

data = np.loadtxt("area_pri.txt")
area, pri = [], []
for x, y in data:
    area.append(x)
    pri.append(y)
plt.bar(area, pri, align='center', alpha=0.5)
plt.xlabel("area")
plt.ylabel("price")

plt.show()
