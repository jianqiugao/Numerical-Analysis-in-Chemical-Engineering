import matplotlib.pyplot as plt
import numpy as np
num = 5
num = num*3 # 点必须是3的倍数
x = np.linspace(-2,8,num)

fx = lambda m: m**2 - 3*m + 2 # 导数函数
fx = fx(x)# 导数


FX = 1/3.*(x**3)-3/2.*x**2 +2*x + 2
delt_h = x[2]-x[1]
def simpson(y):
    """

    :param y:
    :return:
    """
    y_1 = y[:-2][::2]
    y_2 = y[:-1][1::2]
    y_3 = y[2::2]

    return (y_1+4*y_2+y_3)*delt_h/3


F_num = np.concatenate([np.array([FX[0]]),simpson(fx)])
F_num = np.cumsum(F_num)
plt.plot(x, FX)
plt.plot(x[::2],F_num)
plt.legend(['acc','num'])
plt.scatter(x, FX)
plt.scatter(x[::2],F_num)
plt.show()