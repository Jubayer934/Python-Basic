class phone:
    def call(self):
        print("You can call")

    def message(self):
        print("You can message")

class mobile(phone):  
    '''inheriting phone class
    mobile is a sub class or child class of phone class

    and phone class is base class or super class.
    '''
    def photo(self):
        print("You can take photo")


p=phone()
p.message()
p.call()

q=mobile()
q.message()
q.call()
q.photo()

print(issubclass(mobile,phone))
print(issubclass(phone,mobile))




