def number(x):
    return x%2==0

num=[1,2,3,4,5]

result=list(filter(lambda x: x%2==0,num))

print(result)

print(num)

result=list(filter(number,num))
print(result)