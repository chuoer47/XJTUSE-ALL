import numpy as np
from matplotlib import pyplot as plt

# ## 绘图函数简介

# ### 对数坐标图
#%fig=低通滤波器的频率响应：算术坐标（左上）、X轴对数坐标（右上）、Y轴对数坐标（左下）、双对数坐标（右上） 
w = np.linspace(0.1, 1000, 1000)
p = np.abs(1/(1+0.1j*w)) # 计算低通滤波器的频率响应

fig, axes = plt.subplots(2, 2)
functions = ("plot", "semilogx", "semilogy", "loglog")

for ax, fname in zip(axes.ravel(), functions):
    func = getattr(ax, fname)
    func(w, p, linewidth=2)
    ax.set_ylim(0, 1.5)
plt.show()




# ### 柱状图
#%fig=中国男女人口的年龄分布图
data = np.loadtxt("china_population.txt")
width = (data[1,0] - data[0,0])*0.4 #❶
plt.figure(figsize=(8, 4))
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
#c1, c2 = plt.rcParams['axes.prop_cycle'][:2]
c1='red'
c2='blue'
plt.bar(data[:,0]-width, data[:,1]/1e7, width, color=c1, label=u"男") #❷
plt.bar(data[:,0], data[:,2]/1e7, width, color=c2, label=u"女") #❸
plt.xlim(-width*1.5, 100)
plt.xlabel(u"年龄")
plt.ylabel(u"人口（千万）")
plt.legend()
plt.show()





# ### 散列图
#%fig=可指定点的颜色和大小的散列
plt.figure(figsize=(8, 4))
x = np.random.random(100)
y = np.random.random(100)
plt.scatter(x, y, s=x*1000, c=y, marker=(5, 1), 
            alpha=0.8, lw=2, facecolors="none")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.show()



# ### 图像
img = plt.imread("lena.jpg")
print(img.shape, img.dtype)

#%fig=用imread()和imshow()显示图像
img = plt.imread("lena.jpg")
fig, axes = plt.subplots(2, 4, figsize=(11, 4))
fig.subplots_adjust(0, 0, 1, 1, 0.05, 0.05)
axes = axes.ravel()
axes[0].imshow(img)                        #❶
axes[1].imshow(img, origin="lower")        #❷
axes[2].imshow(img * 1.0)                  #❸
axes[3].imshow(img / 255.0)                #❹
axes[4].imshow(np.clip(img / 200.0, 0, 1)) #❺

axe_img = axes[5].imshow(img[:, :, 0])     #❻
plt.colorbar(axe_img, ax=axes[5])

axe_img = axes[6].imshow(img[:, :, 0], cmap="copper") #❼
plt.colorbar(axe_img, ax=axes[6])

for ax in axes:
    ax.set_axis_off()

import matplotlib.cm as cm
cmap_names = list(cm.cmap_d.keys())
print(cmap_names[:5])

#%fig=使用imshow()可视化二元函数
y, x = np.ogrid[-2:2:200j, -2:2:200j]
z = x * np.exp( - x**2 - y**2) #❶

extent = [np.min(x), np.max(x), np.min(y), np.max(y)] #❷

plt.figure(figsize=(10,3))
plt.subplot(121)
plt.imshow(z, extent=extent, origin="lower") #❷
plt.colorbar()
plt.subplot(122)
plt.imshow(z, extent=extent, cmap=cm.gray, origin="lower")
plt.colorbar()
plt.show()





# ### 等值线图
#%fig=用contour(左)和contourf(右)描绘等值线图
y, x = np.ogrid[-2:2:200j, -3:3:300j] #❶
z = x * np.exp( - x**2 - y**2) 

extent = [np.min(x), np.max(x), np.min(y), np.max(y)]

plt.figure(figsize=(10,4))
plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.subplot(121)
cs = plt.contour(z, 10, extent=extent) #❷
plt.clabel(cs) #❸
plt.subplot(122)
plt.contourf(x.reshape(-1), y.reshape(-1), z, 20) #❹;


#  **TIP**
#  如果需要对散列点数据绘制等值线图，可以先使用`scipy.interpolate`模块中提供的插值函数将散列点数据插值为网格数据。

#%fig=使用等值线绘制隐函数曲线（左），获取等值线数据并绘图（右）
y, x = np.ogrid[-1.5:1.5:200j, -1.5:1.5:200j]
f = (x**2 + y**2)**4 - (x**2 - y**2)**2

plt.figure(figsize=(9, 4))
plt.subplot(121)
extent = [np.min(x), np.max(x), np.min(y), np.max(y)]
c_s=["b", "r"]
cs = plt.contour(f, extent=extent, levels=[0, 0.1],    #❶
     colors=c_s, linestyles=["solid", "dashed"], linewidths=[2, 2])


plt.subplot(122)
i=0
for c in cs.collections: #❷
    data = c.get_paths()[0].vertices
    plt.plot(data[:,0], data[:,1], 
        color=c_s[i], linewidth=c.get_linewidth()[0])
    i=i+1
plt.show()




# ### 箭头图
#%fig=用quiver()绘制矢量场
def f(x, y):
    return x * np.exp(- x**2 - y**2)

def vec_field(f, x, y, dx=1e-6, dy=1e-6):
    x2 = x + dx
    y2 = y + dy
    v = f(x, y)
    vx = (f(x2, y) - v) / dx
    vy = (f(x, y2) - v) / dy 
    return vx, vy
plt.figure(figsize=(6, 4))  
X, Y = np.mgrid[-2:2:20j, -2:2:20j]
C = f(X, Y)
U, V = vec_field(f, X, Y)
plt.quiver(X, Y, U, V, C)
plt.colorbar();
plt.gca().set_aspect("equal")
plt.show()


#%fig=使用箭头表示参数曲线的切线方向
plt.figure(figsize=(8, 4))
n = 40
arrow_size = 16
t = np.linspace(0, 1, 1000)
x = np.sin(3*2*np.pi*t)
y = np.cos(5*2*np.pi*t)
line, = plt.plot(x, y, lw=1)

lengths = np.cumsum(np.hypot(np.diff(x), np.diff(y)))
length = lengths[-1]
arrow_locations = np.linspace(0, length, n, endpoint=False)
index = np.searchsorted(lengths, arrow_locations)
dx = x[index + 1] - x[index]
dy = y[index + 1] - y[index]
ds = np.hypot(dx, dy)
dx /= ds
dy /= ds
plt.quiver(x[index], y[index], dx, dy, t[index],
          units="dots", scale_units="dots", 
          angles="xy", scale=1.0/arrow_size, pivot="middle",
          edgecolors="black", linewidths=1,
          width=1, headwidth=arrow_size*0.5, 
          headlength=arrow_size, headaxislength=arrow_size, 
          zorder=100)
plt.colorbar()
plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])
plt.show()

#%fig=使用quiver()绘制神经网络结构示意图
plt.figure(figsize=(7, 4))
levels = [4, 5, 3, 2]
x = np.linspace(0, 1, len(levels))

for i in range(len(levels) - 1):
    j = i + 1
    n1, n2 = levels[i], levels[j]
    y1, y2 = np.mgrid[0:1:n1*1j, 0:1:n2*1j]
    x1 = np.full_like(y1, x[i])
    x2 = np.full_like(y2, x[j])
    plt.quiver(x1, y1, x2-x1, y2-y1, 
              angles="xy", units="dots", scale_units="xy", 
              scale=1, width=2, headlength=10,
              headaxislength=10, headwidth=4)
    
yp = np.concatenate([np.linspace(0, 1, n) for n in levels])
xp = np.repeat(x, levels)
plt.plot(xp, yp, "o", ms=12)
plt.gca().axis("off")
plt.margins(0.1, 0.1)
plt.show()



# ### 三维绘图
#%fig=使用mplot3D绘制的三维曲面图

x, y = np.mgrid[-2:2:20j, -2:2:20j] #❷
z = x * np.exp( - x**2 - y**2)

fig = plt.figure(figsize=(8, 6))
ax = plt.subplot(111, projection='3d') #❸
ax.plot_surface(x, y, z, rstride=2, cstride=1, cmap = plt.cm.Blues_r) #❹
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
