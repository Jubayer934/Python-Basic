'''
Key value
to store data
'''

studentID={
    '101':'Jubayer Al Mahmud',
     102 : 'Noshin'

}
print(studentID['101'])
print(studentID[102])
#print(studentID[106 or '106])  will be error

print(studentID.get('101'))
print(studentID.get(102))
print(studentID.get('106'))
print(studentID.get(106))
print(studentID.get(106,'Have no key'))
print(studentID.get(102,'Have no key'))
