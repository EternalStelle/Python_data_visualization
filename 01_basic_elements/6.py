import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)
plt.plot(x, y,ls="-",lw=2,c="c",label="plot figure")
plt.legend()
#axhline即为绘制平行于x轴的参考线，h即为horizon
#axvline即为绘制平行于y轴的参考线，v即为vertical
plt.axhline(y=0.0,c="r",ls="--",lw=2)
plt.axvline(x=4.0,c="r",ls="--",lw=2)
plt.show()