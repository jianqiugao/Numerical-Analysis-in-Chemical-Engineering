import numpy as np
import matplotlib.pyplot as plt

def function(x:np.ndarray):
    return .02*np.pow(x,3) + 0.105*np.pow(x,2) - 1*x -3

x = np.linspace(-10,10,30)
y = function(x)

plt.scatter(x,y)
plt.axhline(0,c='r')

inter = (y*np.roll(y,-1))[:-1]  # 要去掉最后一个,也就是取前面的n-1
start = np.where(inter<=0)[0] # 找到x1*x2小于等于0的index
end = 1 + start

# 在找到的index,index+1之间继续二分
root = list(zip(start.data,end.data))
print(root)
roots = [] # 做一个列表用来存放这些根
results = []
eps = 0.001
for item in root: # 遍历3个根
    start_x = x[item[0]]
    end_x = x[item[1]]
    while True:
        middle_x = start_x + (end_x-start_x)/2
        start_y = function(start_x)
        middle_y = function(middle_x)
        if np.abs(start_y) < eps: #达到允许的值的时候
            roots.append(start_x)
            results.append(start_y)
            print('find root')
            break
        if start_y*middle_y> 0: # 大于0的时候要
            start_x = middle_x
            end_x = end_x
        else:
            start_x = start_x
            end_x = middle_x
plt.plot(x,y)
plt.axhline(0,c='r')
plt.scatter(roots,results)
print(results)
plt.show()