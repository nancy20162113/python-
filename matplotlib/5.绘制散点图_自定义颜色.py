#author='zhy'
#author='zhy'
import matplotlib.pyplot as plt
x_values=[1,2,3,4,5]
y_values=[1,4,9,16,25]

#1.参数c指定颜色
#plt.scatter(x_values,y_values,c='red',s=100)

#2.RGB,元组，三个0-1的小数，分别表示红色、绿色和蓝色的分量
#plt.scatter(x_values,y_values,c=(0.8,0.8,0.2),s=100)

#3颜色映射，一系列颜色，从起始颜色渐变到结束颜色
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=100)

#设置图标标题并给坐标轴加上标签
plt.title("Square Numbers",fontsize=14)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Values",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=14)



plt.show()