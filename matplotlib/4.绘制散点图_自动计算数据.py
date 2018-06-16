#author='zhy'
import matplotlib.pyplot as plt
x_values=range(1,1001)
y_values=[x**2 for x in x_values]

plt.scatter(x_values,y_values,s=10)

#设置图标标题并给坐标轴加上标签
plt.title("Square Numbers",fontsize=14)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Values",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=10)

#设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])

plt.show()