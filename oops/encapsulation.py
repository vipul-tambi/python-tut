class Student:
    def __init__(self):
        self.__name="" # __ is use dto make variable private

    def getname(self):
      return  self.__name
    
    def setname(self,name):
       self.__name=name


obj=Student()
obj.setname("bchvc")
print(obj.getname())



class S:
    __name="jbhvjgc"
    def __init__(self):
      print(self.__name)
      self.__displayinfo()
    def displayinfo(self):
      print("Welcome")

obj=S()
