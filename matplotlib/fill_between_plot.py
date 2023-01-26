import matplotlib.pyplot as plt
import numpy as np


x=np.array([1,2,3,4,5])
y=np.array([1,2,3,4,5])

plt.plot(x,y,color="r")

plt.fill_between(x,y,color="g", where= (x>=2) &(x<=4),alpha=0.5)



plt.title("Fill Between")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
