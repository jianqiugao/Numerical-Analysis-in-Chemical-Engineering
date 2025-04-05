import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2,8,20)
f1 = lambda m,y1 : m**2 - 3*m + 2 -y1 # 导数函数

y1_0 = 1
delta_h = x[1]-x[0]

sol = [y1_0]
for index,itrm in enumerate(x): # 拿到x
    k1 = delta_h * f1(itrm,y1_0)
    k2 = delta_h * f1(itrm + 1 / 2. * delta_h,y1_0+1/2.*k1)
    k3 = delta_h * f1(itrm + 1 / 2. * delta_h,y1_0+1/2.*k2)
    k4 = delta_h * f1(itrm + delta_h,y1_0+k2)
    y1_0 = y1_0 + 1 / 6. * (k1 + 2 * k2 + 2 * k3 + k4)  # 欧拉法计算
    sol.append(y1_0)

plt.plot(x,sol[:-1])
plt.legend(['rung-kuta'])
plt.show()