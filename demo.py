#print
print("Welcome")
print("Hey Boii!!","How are You?")
print(10+12)
print(10>5)

#variable name should not contain spaces 
#variable name must start with alphabet
#variable

a=10
b=10
print(a,b)
print(id(a),id(b)) #used to get address

a="hello"
b="boiii"
print(a+b)


#Arithmetic operators
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(b%3)
print(5**4)
print(5//3)



#Assignment operators
#+=   -=     =

#Comparisom=n
# ==
# !=
# >
# <
# >=
# <=



#Logical Operators
# and
# or
# not



#membershipOperators
# in 
# not in

string1="Hello"
print('H' in string1)

l=[10,20,30,40]
print(50 not in l)


# is
# not is
x=10
y=10
print(x is y)
print (x is not y)


#Bitwise operators
# | or
# & and
# ^ xor

x=10
y=8
print(bin(x)) # used to get binary
print(bin(y))



#nuumbers
a=5
print(a,type(a))
a=5.5
print(a,type(a))
a=2+5j
print(a,type(a))


s="Hello"
print(a,type(s))

#taking user input
# a=input("Enter the value1 :-")
# b=input("Enter the value2 :-")
# print(a+b)


# a=int(input("Enter v1:-"))
# b=float(input("Enter v2:-"))



# IF ELSE ELIF
#Always use with proper indentation

# per=int(input("Enter percentage :-"))
# if per>=75:
#     print("First")
# elif per>=60:
#     print("Second")
# elif per>=33:
#     print("Third")
# else:
#     print("Four")


#range
#range(1,6) start=1 condition<6 tcrement=1  

for n in range(5):
    print(n)

print()

for n in range(1,6):
    print(n)

print()

for n in range(1,6,2):
    print(n)

for n in range(10,-1,-2):
    print(n)


#while loop
i=1
while i<=10:
    print(i,"Hi")
    i+=1
print(i)

#string
s="Hello Buddy!"
print(s[1])
print(s[-1])

print(s[0:7])
print(s[0::2])
print(s[-1::-1])


w="Welcome to Wscubetech"
t=len(w)
for a in range(t):
    print(w[a])

#lower, upper ,title,capitalize
print(w.lower())
print(w.upper())
print(w.title())
print(w.capitalize())

#find, index ,isalpha, isdigit,isalpha
w="Welcome"
print(w.find('e'))
print(w.find('e',2))
print(w.find('z'))

#chr , ord
a=65
print(chr(a))
y=ord('A')
print(type(y),y)

w="Welocom {} to {} ".format("hello",20)
print(w)



#list - mutable
l=[10,20,30,40,"Hello"]
print(l[3],l[4])
print(l[0:2])
print(l[0::2])
print(l[3:])
print(l[-1::-2])


for a in l:
    print(a)


#List functions
# del -used to pop element from list by passing its index
# remove() -used to remove element from list by passing its value
# pop() -used to pop element from list by passing its index 
# clear() -used to empty the list

l=[10,20,30,40,50,60]
print(l)

del l[1]
print(l)

l=[10,20,30,40,50,60]
print(l.pop(2))


l=[10,20,30,40,50,60]
print(l.remove(40))


l=[10,20,30,40,50,60]
l.clear()


# insert()
# append()
# extends() 

l=[20,30,40,50]
l.insert(0,10)
print(l)


l=[20,30,40,50]
l.append(70)
n=[20,60]
l.append(n)
print(l)

l=[20,30,40,50]
n=[20,40]
l.extend(n)
print(l)


l=[]
for a in range(1,101):
    l.append(a)

print(l)

n=[m for m in range(1,101)]
print(n)

n=[m for m in range(1,101) if m%2==0]
print(n)

s="hello"
d=[g for g in s]
print(d)
#count()
# max()
# min()
# sort()
# reverse()
# index()

l=[10,20,30,10,40,20,10]
print(l.count(10))

m=max(l)
print(m)

m=min(l)
print(m)
l=["Hello" , "World"]
m=max(l)
print(m)

m=min(l)
print(m)

l=[10,20,30,10,40,20,10]
l.sort()
print(l)

l=[10,20,30,10,40,20,10]
l.reverse()
print(l)

l=[10,20,30,10,40,20,10]
print(l.index(30))


#zip function

# l=[1,2,3,4,5]
# l1=[11,12,13,14]
# t=len(l)
# for a,b in zip(l,l1):
#     print(a,b)

# n=input("Enter th value")
# l=n.split()
# print(l)


#stack and queue

#dictionary
d={
    'name':'python',
    'fees' : 8000,
    'duration':'2 Months'
}

print(type(d))
for n in d:
    print(n,d[n])

# dictionary functions
# get()
# keys()
# values()
# items()

n=d.get('name')
print(n)
n=d['name']
print(n)

for a in d.keys():
    print(a)

for a in d.values():
    print(a)


for a,b in d.items(): #a=key , b=value
    print(a,b)

#delete dictionary values
#del
#pop()

del d['name']
print(d)    

d.pop('duration')
print(d)

d=dict(name='python',duration='2 Months')
print(d)

d.update({'duration':'3 months'})

d.clear()
print(d)

course={
    'php':{'duration' :  '3 Months','fees' : 8000},
    'python':{'duration' :  '2 Months','fees' : 9000},
    'java':{'duration' :  '4 Months','fees' : 10000}



}
print(course['php'])
for k,v in course.items():
    print(k,v)
course['java']['fees']=0
for k,v in course.items():
    print(k,v)


#tuple
#()
#min() ,max() , index() ,sum () ,count()


#sets
# set()
# add()
# pop()
# remove()
# clear()
# discard()
# update()

l=[10,20,30]
s=set(l)
print(s)

s.add(40)
print(s)

s.pop() #reandomly delete any number
print(s)


s=set(l)
s.remove(10)
print(s)


s=set(l)
s.discard(20)
print(s)


s.clear()
print(s)

s={10,20,30}
l=[30,40,50]
s.update(l)
print(s)

def sum(a,b):
    return a+b

s=sum(10,20)
print(s)

#import math
# math.ceil()
# math.floor()
# math.fabs()
# math.fsum()
# math.factorial()




#import random
# random.randint(a,b)-random integer between a and b both included
# random.randrange(a,b)-random integer between a (included) and b(not included)
# random.choice(l)- chooses one element from list l
# random.random()- random value between 0 and 1
# random.shuffle()- shuffles the list
# random.uniform()-gives float value between a and b