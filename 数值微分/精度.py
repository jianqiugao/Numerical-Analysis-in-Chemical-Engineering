import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return -2.*(np.power(x,2))-5.+3.*x

f3 = lambda m:(f(3)-f(3-m))/(m)

x = np.arange(0, 18, 0.001,dtype=np.float32)
y = []
for i in x:
    h = 1./(10.**i)
    y.append(f3(h))
# plt.ylim([-12,-6])
plt.plot(x,y)
plt.show()