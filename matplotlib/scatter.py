import matplotlib.pyplot as plt

# day=[1,2,3,4,5,6,7]
# no=[3,2,6,8,2,5,7]
# colors=["r","g","b","y","g","r","g"]
# sizes=[100,120,140,160,180,200,220]
# plt.scatter(day,no,c=colors,s=sizes,alpha=1,edgecolor="b",linewidth=2)
# plt.title("Scatter Plot",fontsize=15)
# plt.xlabel("Day",fontsize=15)
# plt.ylabel("No.",fontsize=15)
# plt.show()

day=[1,2,3,4,5,6,7]
no=[3,2,6,8,2,5,7]
no2=[2,6,3,6,2,5,6]
colors=[10,30,25,60,100,0,50]
sizes=[100,120,140,160,180,200,220]
plt.scatter(day,no,c=colors,s=sizes,alpha=1)
plt.scatter(day,no2,color="r",s=sizes,alpha=0.5)
t=plt.colorbar()
t.set_label("Color Bar",fontsize=15)
plt.title("Scatter Plot",fontsize=15)
plt.xlabel("Day",fontsize=15)
plt.ylabel("No.",fontsize=15)
plt.show()