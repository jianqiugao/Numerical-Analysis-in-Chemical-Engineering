import numpy as np
import matplotlib.pyplot as plt
def P(x):
    return -0.1
def G(x):
    return 1

def R(x):
    return -3.

A = 1.

B = 6.

x_0 = 0
x_max = 10
num = 100
# 划分网格
x = np.linspace(x_0,x_max,num)
inter = (x[1:]-x[:-1])
h = inter[:-1]/2 + inter[1:]/2 # 每个地方的长度可以做成不一样

# 构建矩阵
P_values = P(x[1:-1])
G_values = G(x[1:-1])
R_values = R(x[1:-1])

diag_1 = np.ones(num)
b = np.zeros_like(diag_1)
b[0] = A
b[-1] = B

diag_0 = 2-h*P_values
diag_1[1:-1] = 2*h*h*G_values-4
diag_2 = 2+h*P_values

b[1:-1] = 2*h*h*R_values
A_matrix = np.zeros((num,num))
np.fill_diagonal(A_matrix[1:, :-1], diag_0)
np.fill_diagonal(A_matrix[:-1, 1:], diag_2)
np.fill_diagonal(A_matrix, diag_1)

res = np.linalg.solve(A_matrix,b.reshape(-1,1))

dydx = (res[2:] -res[:-2])/2/h #
dydydxdx = (res[2:] -2*res[1:-1]+ res[:-2])/2/h

residul = np.mean(dydydxdx + P_values*dydx + res[1:-1]*G_values - R_values) # 算一下残差
print(residul)
plt.axhline(A)
plt.axhline(B)
plt.plot(x,res)
plt.show()

print(A_matrix)
