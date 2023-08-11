#柱状图
import matplotlib as mpl
import matplotlib.pyplot as plt
#rcParams设定基础设置
mpl.rcParams["font.sans-serif"]=["SimHei"]
mpl.rcParams["axes.unicode_minus"]=False

x=[1,2,3,4,5,6,7,8]
y=[3,1,4,5,8,9,7,2]

plt.bar(x,y,align="center",color="c",tick_label=["q","a","c","e","r","j","b","p"],hatch="/")

plt.xlabel("箱子编号")
plt.ylabel("箱子重量(kg)")
plt.show()