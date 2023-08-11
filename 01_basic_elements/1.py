# 导入包
import matplotlib.pyplot as plt
import numpy as np

# x=np.linspace(0.5,3.5,100)
# linspace(0.5,3.5,100)代表在0.5和3.5之间均匀取100个数
# y=np.sin(x)
# y1=np.random.randn(100)
# randn(100)代表在标准正态分布中随机取100个数

x = np.linspace(0.05, 10, 1000)
y = np.cos(x)
# ls即线的样式,lw即为线宽度
plt.plot(x, y, ls="-", lw=2, label="plot figure")
# legend即为图例
plt.legend()
plt.show()
