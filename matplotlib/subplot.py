import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[1,2,3,4]
plt.subplot(2,2,1)
plt.plot(x,y,color="r")


plt.subplot(2,2,2)
plt.pie([1],colors="r")


x=[1,2,3,4]
y=[2,3,4,5]


plt.subplot(2,2,3)
plt.bar(x,y)

plt.subplot(2,2,4)
plt.pie(x)


plt.show()


