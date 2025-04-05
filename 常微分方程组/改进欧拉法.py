import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2,8,15)
fx = lambda m: m**2 - 3*m + 2 # 导数函数


delta_h = x[1]-x[0]
FX = 1/3.*(x**3)-3/2.*x**2 +2*x + 2 # 原函数

y0 = FX[0] # 初始值
num_step = 20 # 假设每一步最多迭代这么多步
eps = 0.0000001
sol = [y0]
for index,itrm in enumerate(x): # 拿到导数
    y0_ = y0+fx(itrm)*delta_h # 欧拉法计算
    for step in range(num_step): # 改进隐式迭代,如果函数是隐函数也可以完成迭代
        res = y0_
        y0_ = y0+1/2*delta_h*(fx(itrm)+fx(itrm+delta_h))
        if np.abs(y0_ - res)<eps:
            print(step)
            break
    y0 = y0_

    sol.append(y0)

plt.plot(x, FX)
plt.plot(x,sol[:-1])
plt.legend(['acc','improved euler'])
plt.show()