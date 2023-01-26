import matplotlib.pyplot as plt

x=[1,2,3,4,5,6]
y=[2,5,3,6,2,5]


plt.stem(x,y,linefmt=":",markerfmt="ro",basefmt="k",label="python",orientation="vertical")

plt.legend()
plt.show()