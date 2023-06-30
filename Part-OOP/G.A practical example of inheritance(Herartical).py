'''
working=adding and multiple

'''

class work:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def work1(self):
        print("I am in work method of working class")

class add(work):
    def work(self):
        add=self.a+self.b
        print(" added value is = ",add)

class multi(work):
    def work(self):
        multi=self.a*self.b
        print("the multi value is = ",multi)

a1=add(10,20)
a1.work()

m1=multi(10,20)
m1.work()