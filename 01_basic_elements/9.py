import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)
plt.plot(x, y, ls="-", lw=2, c="c", label="plot figure")
# loc()即为图例的位置
plt.legend(loc="lower left")
# text()即添加无指向的文本
plt.text(3.10, 0.09, "y=sin(x)", weight="bold", color="b")
# title()即标题文本
plt.title("y=sin(x)")
plt.show()
