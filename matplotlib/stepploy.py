import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[2,5,2,6,3]

plt.step(x,y,color="r",marker="o",label="python")

plt.title("python")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.legend()
plt.grid()
plt.show()