import matplotlib.pyplot as plt

x=[1,2,3,4,5]
area=[1,2,3,4,5]
area1=[2,4,6,2,4]
area2=[2,5,6,3,1]

l=["area","area1","area2"]
plt.stackplot(x,area,area1,area2,labels=l,colors=["r","g","m"])


plt.title("python")
plt.xlabel("x-axis")
plt.ylabel("y-label")
plt.legend()
plt.show()