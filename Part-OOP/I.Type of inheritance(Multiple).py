class A:
    def display(self):
        print("I am in A")
    
class B:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print("i am in B")


class C(A,B):
    pass
class D(A,B):
    def display(self):
        print("I am in D")
    def result(self):
        print(self.a+self.b)


Y=D(2,5)
Y.display()
Y.result()
X=C(1,2)
X.display()