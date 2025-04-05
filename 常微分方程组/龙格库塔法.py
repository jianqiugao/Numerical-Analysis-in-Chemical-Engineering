import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2,8,10)
fx = lambda m: m**2 - 3*m + 2 # 导数函数


delta_h = x[1]-x[0]
FX = 1/3.*(x**3)-3/2.*x**2 +2*x + 2 # 原函数

y0 = FX[0] # 初始值
sol = [y0]
for index,itrm in enumerate(x): # 拿到导数
    k1 = delta_h*fx(itrm)
    k2 = delta_h*fx(itrm+1/2.*delta_h)
    k3 = delta_h*fx(itrm+1/2.*delta_h)
    k4 = delta_h*fx(itrm+delta_h)
    y0 = y0+1/6.*(k1+2*k2+2*k3+k4) # 欧拉法计算
    sol.append(y0)

plt.plot(x, FX)
plt.plot(x,sol[:-1])
plt.legend(['acc','rung-kuta'])
plt.show()