i=0

while i<=10:
    i+=1
    if i==4:
        print('no print after that')
        break
    print(i)

print('test continue')
i=0

while i<=10:
    i+=1
    if i==4:
        print('not printing 4')
        continue
    print(i)
