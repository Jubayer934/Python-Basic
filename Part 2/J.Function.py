'''
User define function
'''

def sum(x,y):
    return x+y

def add(x,y,z):
    return x+y+z
def message():
    print("without parameter")
a,b=map(int,input().split())
print(sum(a,b))

a,b,c=map(int,input().split())
print(add(a,b,c))

message()