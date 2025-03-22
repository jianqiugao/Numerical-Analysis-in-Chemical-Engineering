import numpy as np
import matplotlib.pyplot as plt

def function(x:np.ndarray):
    return .02*np.pow(x,3) + 0.105*np.pow(x,2) - 1*x -3

x = np.linspace(-10,10,30)
y = function(x)

def iter_function(x):
    return .02 * np.pow(x, 3) + 0.105 * np.pow(x, 2) - 3


epoch = 100
initial_values = -5
fig,axes = plt.subplots(1,3)

res_list = []
root = []
eps = 0.0001
for i in range(epoch): # 迭代
    iter_x = iter_function(initial_values)
    res = initial_values -iter_x
    initial_values = iter_x
    res_list.append(np.abs(res))
    root.append(initial_values)
    if np.abs(res) < eps:
        break


axes[1].plot(res_list)
axes[1].set_xlabel('iter_num')
axes[1].set_ylabel('residual')
axes[0].scatter(initial_values,function(initial_values))
axes[0].scatter(x,y)
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[2].plot(root)
axes[2].set_xlabel('iter_num')
axes[2].set_ylabel('root')
plt.show()


