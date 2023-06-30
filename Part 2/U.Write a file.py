student=open("student.txt","r+") # r = read, w= write /it will add and remove previous , r+= read and write , a=append add with previous also work with r+



for i in student:
    print(i)

student.write("\nNoshin = 3rd")

student.close()

file=open("student.py","w") #Creating a file
file.write("jubayer")
file.close()