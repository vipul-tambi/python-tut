# class A:
#     def displayA(self):
#         print("Inside A")


# class B(A):
#     def displayB(self):
#         print("Inside B")


# class C(B):
#     def displayC(self):
#         print("Inside C")

class A:
    def displayA(self):
        print("Inside A")


class B:
    def displayB(self):
        print("Inside B")


class C(A,B):
    def displayC(self):
        print("Inside C")


obj=C()
obj.displayA()
obj.displayB()
obj.displayC()

