import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2,8,6)
delta_h = 0.2
fx = lambda m: m**2 - 3*m + 2 # 导数函数
fx = fx(x)# 导数
x_0 = 0
FX = 1/3.*(x**3)-3/2.*x**2 +2*x + 2
delt_h = x[2]-x[1]
def trip(y_1,y_2,delt_h):
    """
    计算梯形的面积
    :param y_1:
    :param y_2:
    :param delt_h:
    :return:
    """
    return (y_1+y_2)*delt_h/2

F_num = np.concatenate([np.array([FX[0]]),trip(fx[:-1],fx[1:],delt_h)])
F_num = np.cumsum(F_num)

plt.plot(x, FX)
plt.plot(x,F_num)
plt.legend(['acc','num'])
plt.show()