'''
__lt__=less than
__le__=less eq.
__eq__=equal
__ne__=not equal
__gt__=greater than
__ge__=greater than or equal
__add__
__sub__
__mul__
__div__
'''

class bike:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def __str__(self):
         return (f"Name = {self.name} , color = {self.color}")
    
    def __eq__(self,other):
        return self.name == other.name and self.color == other.color
    
    def __ne__(self,other):
        return self.name!=other.name and self.color != other.color
    
    def display(self):
        print(f"Name = {self.name} , color = {self.color}")

bike1 = bike("Yamaha R15","Blue")
bike2 = bike ("Yamaha R15","Blue")
bike3=bike("4V","Red")
print(bike1)

print(bike1==bike2)
print(bike1!=bike3)
