num=[1,2,3,4,5]


# [ expression for item in list]=system
result = list (map(lambda x : x*x,num))

print(result)

'''

List comprehenssion

'''

result=[i*i for i in num]

print(result)


'''
filting with comprehensions
'''

result=[x*x for x in num if x%2==0]
print(result)