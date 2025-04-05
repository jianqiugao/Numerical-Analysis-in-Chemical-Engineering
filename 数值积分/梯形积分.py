import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2,8,15)
fx = lambda m: m**2 - 3*m + 2 # 导数函数
fx = fx(x)# 导数


FX = 1/3.*(x**3)-3/2.*x**2 +2*x + 2 # 原函数


delt_h = x[2]-x[1]
def trip(y):
    """

    :param y:
    :return:
    """
    y_1 = y[:-1]
    y_2 = y[1:]
    return (y_1+y_2)*delt_h/2

F_num = np.concatenate([np.array([FX[0]]),trip(fx)])
F_num = np.cumsum(F_num)

plt.plot(x, FX)
plt.plot(x,F_num)
plt.legend(['acc','num'])
plt.show()