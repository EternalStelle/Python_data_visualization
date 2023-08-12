# 气泡图，二维数据借助气泡的大小显示三维数据
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
a=np.random.rand(100)
b=np.random.rand(100)

plt.scatter(a,b,s=np.power(10*a+20*b,2),
            c=np.random.rand(100),
            cmap=mpl.cm.RdYlBu,
            marker="o")

plt.show()