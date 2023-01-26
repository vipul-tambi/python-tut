import matplotlib.pyplot as plt


# x=[10,20,30,40]
# y=["c","c++","java","python"]
# c=["r","w","g","y"]
# ex=[0.3,0.0,0.0,0.0]
# plt.pie(x,labels=y,colors=c,explode=ex,autopct="%0.1f%%",shadow=True,radius=1.5,labeldistance=1.1,startangle=0,
#         counterclock=False,textprops={"fontsize":20},wedgeprops={"edgecolor":"k"})


# plt.title("Tutorial")
# plt.show()




x=[10,20,30,40]
y=["c","c++","java","python"]
c=["r","w","g","y"]
ex=[0.3,0.0,0.0,0.0]
plt.pie(x,labels=y,radius=1.5)
plt.pie([1],colors="w")

plt.title("Tutorial")
plt.show()

