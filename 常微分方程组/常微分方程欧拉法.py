import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2,8,20)
fx = lambda m: m**2 - 3*m + 2 # 导数函数
fx_results = fx(x)# 导数

delta_h = x[1]-x[0]
FX = 1/3.*(x**3)-3/2.*x**2 +2*x + 2 # 原函数

x0 = FX[0]
sol = [x0]
for index,itrm in enumerate(fx_results): # 拿到导数
    x0 = x0+itrm*delta_h
    sol.append(x0)



plt.plot(x, FX)
plt.plot(x,sol[:-1])
plt.legend(['acc','euler'])
plt.show()