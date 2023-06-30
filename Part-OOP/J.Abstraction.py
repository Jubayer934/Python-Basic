from abc import ABC,abstractmethod

class work(ABC):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    @abstractmethod
    def work1(self):
        pass
'''
Must have to use the method of perents class
'''
class add(work):
    def work1(self):
        add=self.a+self.b
        print(" added value is = ",add)

class multi(work):
    def work1(self):
        multi=self.a*self.b
        print("the multi value is = ",multi)

a1=add(10,20)
a1.work1()

m1=multi(10,20)
m1.work1()