# 极坐标线图
import matplotlib.pyplot as plt
import numpy as np

barSlices = 12
# endpoints参数默认为True
# 若不想在计算中包含最后点(默认包含)，则设置endpoints为False
theta = np.linspace(0.0, 2 * np.pi, barSlices, endpoint=False)
r = 30 * np.random.rand(barSlices)
plt.polar(theta, r, 
          color="chartreuse", 
          linewidth=2, 
          marker="*", 
          mfc="b", 
          ms=10)
plt.show()
