class phone:
    def __init__(self):
        print("I am in phone class")


class mobile1(phone):
    def __init__(self):
        super().__init__()
        print("I am in samsung class")

class mobile2(phone):
    pass

class mobile3(phone):
    def __init__(self):
        print("I am in mobile3")

m = mobile1()
n=mobile2()
o=mobile3()
