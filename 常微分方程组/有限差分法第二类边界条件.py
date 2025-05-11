import numpy as np
import matplotlib.pyplot as plt
def P(x):
    return 2/x
def G(x):
    return -5

def R(x):
    return 0

A = 0

B = 1

x_0 = 0.1
x_max = 2
num = 5

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
diag_0 = (2-h*P(x[1:-1]))
np.fill_diagonal(matrix_A[1:-1, :-2], diag_0)
diag_1 = (2*(h**2)*G(x[1:-1])-4)
np.fill_diagonal(matrix_A[1:-1, 1:-1], diag_1)
diag_2 = 2+h*P(x[1:-1])
np.fill_diagonal(matrix_A[1:-1, 2:], diag_2)
matrix_A[-1,-1] = 1
res = np.linalg.solve(matrix_A,b.reshape(-1,1)).reshape(-1)

res[1] = (res[0]+res[1])/2
x[1] = (x[0]+x[1])/2
plt.axhline(A)
plt.axhline(B)
plt.plot(x[1:],res[1:])
plt.show()

print(matrix_A)
print(b)