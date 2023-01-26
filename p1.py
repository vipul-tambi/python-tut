import numpy as np

x=[1,2,3,4]
y=np.array(x)
y
print(y)
print(type(y))


ar2=np.array([[1,2,3,4,],[1,2,3,4]])
print(ar2)
print(ar2.ndim)

ar_zero=np.zeros(4)
ar_zeros=np.zeros((3,4))
print(ar_zero)
print(ar_zeros)


ar_one=np.ones(4)
ar_ones=np.ones((3,4))
print(ar_one)
print(ar_ones)

ar_em=np.empty(4)
print(ar_em)

ar_range=np.arange(4)
print(ar_range)

#rand -> between 0 and 1
#randn -> close to zer
#ranf -> [0.0,1.0)]
#randint -> between range
var1=np.random.rand(5)
print(var1)

var2=np.random.randn(10,2)
print(var2)

var3=np.random.ranf(5)
print(var3)

#var4=np.random.randint(min,max,total)
var4=np.random.randint(5,20,6)
print(var4)


a1=np.array([1,2,3,4])
print(a1+1)

a1=np.array([1,2,3,4])
a2=np.array([1,7,89,9])
print(a1*a2)


a1=np.array([[1,2,3,4],[1,2,3,4]])

var =np.array([1,2,3,4,78,254,36,2,2,3,46,2,1])
print("min : ",np.min(var),np.argmin(var))
print("max : ",np.max(var),np.argmax(var))

#axis 0 Col
#axis 1 Row

var =np.array([[1,4,8,],[1,6,4]])
print(np.min(var,axis=0))

var =np.array([1,2,3,4,78,254,36,2,2,3,46,2,1])
print("sqrt : ",np.sqrt(var))
print("sin : ",np.sin(var))
print("cos : ",np.cos(var))
print("cumsum : ",np.cumsum(var))



#shape
var1=np.array([[1,2,2],[1,2,3]])
print(var1.shape)
var1=np.array([1,2,3,4],ndmin=4)
print(var1.ndim)
print(var1.shape)
print(var1)

#reshape
var2=np.array([1,2,3,4,5,6])
print(var2)
print(var2.ndim)

print()

x=var2.reshape(3,2)
print(x)
print(x.ndim)

print()

x=x.reshape(-1)
print(x)
print(x.ndim)


x=np.array([[1],[2]])
y=np.array([[1,2,3],[1,4,5]])


print(x+y)



var =np.array([1,2,3,4])
#indexing      0,1,2,3
#             -4,-3,-2,-1


#slicing in numpy arrays
#x[start:stop:step]

x=np.array([1,2,3,4,5,6,7,8,9])
print(x[1:8])

x=np.array([[[1,2,3,4,5],[3,6,2,5,6],[3,0,5,7,8]]])
#print(x[1,1:])

for i in x:
    print(i)


for i in x:
    for j in i:
        print(j)


#nditer()
for i in np.nditer(x):
    print(i)


#ndenumerate()
for i,d in np.ndenumerate(x):
    print(i,d)


#copy vs view
var =np.array([1,2,3,4,5])
co=var.copy()

print(co)

vi=var.view()
print(vi)

#copy ka khud ka data hota h view ka khud ka data nhi hota



#Join array
#concatenate
var=np.array([1,2,3,4])
var1=np.array([7,8,9,0])
v=np.concatenate((var,var1))

var=np.array([[1,2],[3,4]])
var1=np.array([[7,8],[9,0]])

v=np.concatenate((var,var1),axis=0)
print(v)


#search sort filter

#search
var =np.array([1,4,9,24,76,4,7,3,7,4,6,6,3,7,4,4])
x=np.where(var%2==0)
print(x)

#sort
print(np.sort(var))

#filter
var=np.array(["a","b","c","d","e","f"])
f=[True,False,False,False,True,False]

new_a=var[f]
print(new_a)


#shuffle
#unique
#resize
#


var=np.array([1,2,3,4,5,6,2,4,5])
np.random.shuffle(var)
print(var)

print(np.unique(var))
print(np.unique(var,return_index=True,return_counts=True))  


var=np.array([[1,23,4,4],[1,3,5,4]])
print(var.flatten(order="F"))
print(var.flatten(order="C"))

print(var.ravel(order="K"))





#insert and append
var=np.array([1,5,2,7,4,7])
v=np.insert(var,2,5)
print(v)

v=np.append(v,8)
print(v)

var=np.array([[1,2,3,4],[5,4,7,8]])
v=np.insert(var,2,3,axis=0)
print(v)

var=np.array([[1,2,3,4],[5,4,7,8]])
v=np.insert(var,2,[5,6],axis=1)
print(v)

var=np.array([[1,2,3,4],[5,4,7,8]])
v=np.append(var,[[1,2,3,8]],axis=0)
print(v)



#delete
var=np.array([1,2,3,45,4,7,8])
v=np.delete(var,5)
print(v)


#matrix
var =np.matrix([[1,2,3],[4,5,6]])
print(var)
print(type(var))


var2=np.matrix([[2,3,4],[1,2,3],[1,2,3]])

print(var*var2)



#transpose
var=np.matrix([[1,2,3],[4,5,6]])
print(var)
print()
print(np.transpose(var))
print(var.T)# same as np.transpose(var)


#swapaxes

#inverse of matrix
var=np.matrix([[1,2],[3,4]])
print(np.linalg.inv(var))


#power of a matrix
print(np.linalg.matrix_power(var,3))
print(np.linalg.matrix_power(var,0))
print(np.linalg.matrix_power(var,-3))


#determinant
var=np.matrix([[1,2,3],[4,5,6],[1,8,9]])
print(np.linalg.det(var))