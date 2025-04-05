import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,7,15)
y = -3*x**2 +18*x +1

plt.plot(x,y)
plt.scatter(x,y)
plt.scatter(x[10],y[10],c='r',marker='s')
plt.annotate('marker',[x[10],y[1]])
# plt.show()

# 选择好区间
x_to_inter = x[10]
x_min = x[np.where(x<x_to_inter)][-1]
x_max = x[np.where(x>x_to_inter)][0]
y_min = y[np.where(x<x_to_inter)][-1]
y_max = y[np.where(x>x_to_inter)][0]
plt.axvline(x_min,c='r',linestyle='--')
plt.annotate('x_(i-1)',[x_min,y.min()])

plt.axvline(x_max,c='r',linestyle='--')
plt.annotate('x_i',[x_max,y.min()])
# plt.show()
# 插值
y_to_inter = (x_to_inter-x_max)/(x_min-x_max)*y_min+(x_to_inter-x_min)/(x_max-x_min)*y_max

plt.scatter(x_to_inter,y_to_inter)
plt.plot([x_min,x_max],[y_min,y_max])
plt.xlim([4,6])
plt.show()

