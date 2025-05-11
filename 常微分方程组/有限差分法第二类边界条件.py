import numpy as np
import matplotlib.pyplot as plt
def P(x):
    return -0.5
def G(x):
    return -1

def R(x):
    return -1.

A = -0.0

B = -1.

x_0 = 0
x_max = 10
num = 100
# 划分网格
x = np.linspace(x_0,x_max,num)


# x =

inter = (x[1:]-x[:-1])
h = inter[:-1]/2 + inter[1:]/2 # 每个地方的长度可以做成不一样
# 制作矩阵
matrix_A = np.zeros((num,num))
b = np.zeros(num)
# 添加边界处理
matrix_A[0,[0,1]] =[-1,1] #
b[0] = h[0]*A
b[1:-1] =2*(h**2)*R(x[1:-1])
b[-1] = B
diag_0 = (2-h[:-1]*P(x[1:-2]))
np.fill_diagonal(matrix_A[1:-1, :-2], diag_0)
diag_1 = (2*(h[:-1]**2)*G(x[1:-2]-4))
np.fill_diagonal(matrix_A[1:-1, 1:-1], diag_1)
diag_2 = 2+h[:-1]*P(x[1:-2])
np.fill_diagonal(matrix_A[1:-1, 2:], diag_2)
matrix_A[-1,-1] = 1
res = np.linalg.solve(matrix_A,b.reshape(-1,1))
plt.axhline(A)
plt.axhline(B)
plt.plot(x,res)
plt.show()

print(matrix_A)