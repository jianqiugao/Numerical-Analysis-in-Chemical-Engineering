import numpy as np
import matplotlib.pyplot as plt

def function(x:np.ndarray):
    return .02*np.pow(x,3) + 0.105*np.pow(x,2) - 1*x -3

x = np.linspace(-10,10,30)
y = function(x)

plt.scatter(x,y)
plt.axhline(0,c='r')

# 方法一,选择y值接近0的值
sol = np.abs(y) < 1.1 # 前面已经计算过这个值了，这里直接选就可以了
plt.scatter(x[sol],y[sol])
plt.show()

# 加一点技巧，两个值的y值相乘小于0就作为一个区间
# 方法2 选出y1*y2 小于0的区间,区间开始的值就是根
inter = (y*np.roll(y,-1))[:-1]  # 要去掉最后一个,也就是取前面的n-1
start = np.where(inter<0)[0]
end = 1 + start

inter_start = x[start] # 这个开始的值就是求解的根
plt.scatter(x,y)
plt.scatter(x[start],y[start],c='r')
plt.scatter(x[end],y[end],c='b')

plt.axhline(0,c='r')
plt.show()
print('hello')