import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,7,15)
y = -3*x**2 +18*x +1
plt.plot(x,y)
# 假设待处理的点
x_to_inter = x[10]

y = y[np.abs(x-x_to_inter)>0.0001]
x = x[np.abs(x-x_to_inter)>0.0001] # 由于插值是在这里面选择的把原来有的x剔除

y_to_inter = 0 # 处理连加部分
for index,(x_i,y_i) in enumerate(zip(x,y)):
    m = 1 # 做一个中间变量存储连乘部分
    for j in range(x.shape[0]):
        if j!=index:
            m = m*(x_to_inter-x[j])/(x_i-x[j])
    y_to_inter = y_to_inter + y_i*m

plt.scatter(x_to_inter,y_to_inter)
plt.show()


