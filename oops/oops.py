class DemoClass:  #Always use camel case 
    a=10

    def __init__(self):
        print("WELCOME")

    def sumValue(self): #always give atleast one argument whenever a function is defined inside a classs
        print(20+30)

    def showValue(self):
        print(self.a)
        self.c=self.a*self.a
        print(self.c)

    def showValue1(self,a,b):
        print(a*b)


demoObject=DemoClass()

print(demoObject.a)

demoObject.sumValue()
demoObject.showValue()
demoObject.showValue1(2,8)