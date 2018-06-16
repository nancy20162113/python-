#author='zhy'
import matplotlib.pyplot as plt

x_values=[1,2,3,4,5]
y_values=[x**3 for x in x_values]

#plt.scatter(x_values,y_values,c='red',s=100)
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Reds,s=100)

plt.title("Cubic",fontsize=14)

plt.xlabel("Value",fontsize=14)
plt.ylabel("Cubic of Value",fontsize=14)

plt.show()
