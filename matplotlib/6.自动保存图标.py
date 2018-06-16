#author='zhy'
import matplotlib.pyplot as plt
x_values=[1,2,3,4,5]
y_values=[1,4,9,16,25]

plt.scatter(x_values,y_values,s=100)

#设置图标标题并给坐标轴加上标签
plt.title("Square Numbers",fontsize=14)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Values",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=14)

#自动保存图片
#plt.show()
plt.savefig("squares_scatter.png",bbox_inches='tight')