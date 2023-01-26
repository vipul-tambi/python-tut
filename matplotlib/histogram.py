import matplotlib.pyplot as plt
# import numpy as np
# import random
# x=np.random.randint(10,60,(50))
# print(x)


no=[35 ,36 ,24, 22 ,22 ,26 ,51, 23, 28, 24, 50 ,54, 58, 31 ,25 ,50 ,56, 53, 18 ,51 ,54 ,13 ,10, 31,
 25, 19, 38, 25, 54 ,45 ,51, 19 ,47, 52, 11, 59, 55 ,20, 41, 34, 52, 53, 24 ,28 ,54, 21 ,54 ,10,
 43, 59]

plt.hist(no,edgecolor="k",color="y",label="python")# cumulative=1 cumulative=-1    bottom=10   align      histtype="step", "bar" , "barstack"   orientation="horizontal"     log=True
plt.legend()
plt.title("wscube")
plt.xlabel("python")
plt.ylabel("No.")
plt.axvline(45,color="b")
plt.show()