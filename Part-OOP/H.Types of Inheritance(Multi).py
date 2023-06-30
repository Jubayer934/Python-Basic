'''
Multi level Inheritance
'''

class A:
    def display1(self):
        print("I am in A")
    
class B(A):
    def display2(self):
        print("i am in B")

class C(B):
    def display3(self):
        super().display1()
        super().display2()
        print("i am in C")

X=C()
X.display1()
X.display2()
X.display3()