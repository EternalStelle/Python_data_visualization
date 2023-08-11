import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)
plt.plot(x, y,ls="-",lw=2,c="c",label="plot figure")
plt.legend()
#annotate添加对某个细节的指向性注释
#xy即被注释的位置坐标
#xytext即注释文本的位置坐标
#weight即字重
#arrowprops即箭头的属性
plt.annotate("maximum",
             xy=(np.pi/2,1.0),
             xytext=((np.pi/2)+1.0,.8),
             weight="bold",
             color="b",
             arrowprops
             =dict(arrowstyle="->",connectionstyle="arc3",color="b"))
plt.show()