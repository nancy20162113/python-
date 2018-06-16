#author='zhy'
import matplotlib.pyplot as plt

plt.scatter(2,4,s=100)

#设置图标标题并给坐标轴加上标签
plt.title("Square Numbers",fontsize=14)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Values",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=14)

plt.show()