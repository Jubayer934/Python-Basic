subject= ['c','C++','Java','python','OS']

print(len(subject))

subject.append('TOC')
print(subject)

subject.insert(2,'BASIC')
print(subject)

subject.remove('BASIC')
print(subject)

subject.sort()
print(subject)

subject.reverse()
print(subject)

subject.pop()
print(subject)

subject.pop()
subject.pop()
print(subject)

print(subject.pop())

subject.clear()

print(subject)

subject2=[1,2,3,4,4]

subject=subject2
print(subject)

P=subject.index(3)
print(P)

C=subject.count(4)
print(C)

