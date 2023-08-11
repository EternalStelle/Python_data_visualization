import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)
# 其中的c即为color颜色
plt.plot(x, y, ls="-", lw=2, c="c", label="plot figure")
plt.legend()
# xlabel即为x坐标的标记
plt.xlabel("x_axis")
plt.ylabel("y_axis")
plt.show()
