'''
Triangle
~Contructor
      -base
      height
~calculate area

~T1(10,20)
T2(20,30)
'''
class triangle:

    def __init__(self,base,height):
        self.base=base
        self.height=height

    def cal_area(self):
        area=0.5*self.base*self.height
        print(f"Te area is {int(area)}")


t1=triangle(10,20)
t2=triangle(20,30)


t1.cal_area()
t2.cal_area()