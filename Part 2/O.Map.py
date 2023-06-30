# Map function work with list

num=[1,2,3,4,5]

def sq(x):
    return x*x


result = list(map(sq,num))

print(result)