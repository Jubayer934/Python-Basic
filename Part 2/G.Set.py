num= {1,2,3,4,4,5}

print(num)
#printing numbers but more than one time
num2=[5,6,7]
print(num2)
num22= set(num2)
print(num22)
#list to set

num22.add(3)
num22.add(4)
print(num22)
num22.remove(3)
#Adding and removing
print(num22)

print(4 in num22)
print(8 not in num22)

print(num | num22) #Union

print(num & num22) #intersection

print(num - num22) #Not printing common but only uncommons of NUM