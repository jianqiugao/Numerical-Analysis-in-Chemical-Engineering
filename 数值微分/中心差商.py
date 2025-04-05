import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return -2.*(np.power(x,2))-5.+3.*x + 1*(x**3)
def f_delta(x):
    return -4.*x +3 +3*(x**2)
delta_h = 0.2
f3 = lambda m:(f(x+delta_h)-f(x-delta_h))/(2*delta_h)

x = np.linspace(-2,6,100)
f_delta_acc = f_delta(x)
f_delta_num = f3(x)

plt.plot(x,f_delta_acc)
plt.plot(x,f_delta_num)
plt.legend(['acc','num'])
plt.show()