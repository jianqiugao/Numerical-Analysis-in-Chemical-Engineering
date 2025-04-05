import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 8, 20)
f1 = lambda m, y1, y2: m ** 2 - 3 * m + 2 - y1 + y2  # 导数函数m代表x，n代表y1，y2代表y2
f2 = lambda m, y1, y2: 5 * m - y1 + 2  # 导数函数

y1_0 = 1
y2_0 = 2
delta_h = x[1] - x[0]

sol = [y1_0]
sol_2 = [y2_0]
for index, itrm in enumerate(x):  # 拿到x
    k11 = delta_h * f1(itrm, y1_0, y2_0)
    k21 = delta_h * f2(itrm, y1_0, y2_0)

    k12 = delta_h * f1(itrm + 1 / 2. * delta_h, y1_0 + 1 / 2. * k11, y2_0 + 1 / 2. * k21)
    k22 = delta_h * f2(itrm + 1 / 2. * delta_h, y1_0 + 1 / 2. * k11, y2_0 + 1 / 2. * k21)

    k13 = delta_h * f1(itrm + 1 / 2. * delta_h, y1_0 + 1 / 2. * k12, y2_0 + 1 / 2. * k22)
    k23 = delta_h * f2(itrm + 1 / 2. * delta_h, y1_0 + 1 / 2. * k12, y2_0 + 1 / 2. * k22)

    k14 = delta_h * f1(itrm + delta_h, y1_0 + k13,y2_0+k23)
    k24 = delta_h * f2(itrm + delta_h, y1_0 + k13, y2_0 + k23)

    y1_0 = y1_0 + 1 / 6. * (k11 + 2 * k12 + 2 * k13 + k14)  # 欧拉法计算
    y2_0 = y2_0 + 1 / 6. * (k21 + 2 * k22 + 2 * k23 + k24)  # 欧拉法计算
    sol.append(y1_0)
    sol_2.append(y2_0)

plt.plot(x, sol[:-1])
plt.plot(x, sol_2[:-1])
plt.legend(['y_1','y_2'])
plt.show()