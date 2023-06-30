student=open("student.txt","r+") # r = read, w= write , r+= read and write


text=student.read()


print(student.readable())
print(student.writable())

print(text)
size=len(text)
print(size)

student.close()