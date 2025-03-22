import time

import numpy as np
import matplotlib.pyplot as plt

def function(x:np.ndarray):
    return .02*np.pow(x,3) + 0.105*np.pow(x,2) - 1*x -3

def grad_function(x):
    return 0.06*np.pow(x,2) + 0.21*x -1

x = np.linspace(-10,10,30)
y = function(x)
dy = function(x)
fig,axes = plt.subplots(1,3)
roots = [] # 做一个列表用来存放这些根
results = []
res_list= []
eps = 0.001
start_x = x[15]
start_y = function(start_x)

inter = (y*np.roll(y,-1))[:-1]  # 要去掉最后一个,也就是取前面的n-1
start = np.where(inter<=0)[0] # 找到x1*x2小于等于0的index
end = 1 + start

# 在找到的index,index+1之间用牛顿
root = list(zip(start.data,end.data))

for item in root: # 遍历3个根
    start_x = x[item[0]]
    while True:
        x_1 = start_x-function(start_x)/grad_function(start_x)
        res = np.abs(x_1 -start_x) # 计算残差
        res_list.append(res)
        if res > eps:
            start_x = x_1
        else:
            roots.append(start_x)
            results.append(function(start_x))
            break

axes[1].plot(res_list)
axes[1].set_xlabel('iter_num')
axes[1].set_ylabel('residual')
axes[0].scatter(roots,results)
axes[0].scatter(x,y)
axes[0].axhline(0,c='r')
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')

axes[2].plot(roots)
axes[2].set_xlabel('iter_num')
axes[2].set_ylabel('root')
plt.show()