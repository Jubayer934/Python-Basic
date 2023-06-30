# args = argument

def student(id):
    print(id)


student(101)



def student(*details):
    print(details)


student(101,'jubayer')
# tuples which have first B.=()
student(101,'jubayer',3.34)


def add(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum

print(add(2,3))
print(add(1,2,3,4))