#BAR PLOT
import matplotlib.pyplot as plt
import numpy as np
# x=["python","c","c++","Java"]
# y=[85,70,60,82]


# plt.xlabel("language",fontsize=20)
# plt.ylabel("Number",fontsize=20 )
# plt.title("LEARNING",fontsize=20)
# c=["r","b","y","m"]
# plt.bar(x,y,width=0.4,color=c,edgecolor="k",linewidth=5,alpha=0.7,linestyle=":")
# plt.show(),


########################################################################################

# x=["python","c","c++","Java"]
# y=[85,70,60,82]
# z=[40,45,89,20]
# width=0.2
# p=np.arange(len(x))
# p1=[j+ width for j in p]
# plt.xlabel("language",fontsize=20)
# plt.ylabel("Number",fontsize=20 )
# plt.title("LEARNING",fontsize=20)

# plt.bar(p,y,width,color="r",label="popularity")
# plt.bar(p1,z,width,color="y",label="popularity1")
# plt.xticks(p+width/2,x,rotation=20)
# plt.legend()
# plt.show()

########################################################################################


x=["python","c","c++","Java"]
y=[85,70,60,82]
z=[40,45,89,20]
width=0.2
p=np.arange(len(x))
p1=[j+ width for j in p]
plt.xlabel("language",fontsize=20)
plt.ylabel("Number",fontsize=20 )
plt.title("LEARNING",fontsize=20)

plt.barh(p,y,width,color="r",label="popularity")
plt.barh(p1,z,width,color="y",label="popularity1")
plt.yticks(p+width/2,x,rotation=20)
plt.legend()
plt.show()

