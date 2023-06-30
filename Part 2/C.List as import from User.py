n=input("Enter give some number : ")

list=n.split()

sum=0
for i in list:
    sum=sum+int(i)
print(sum)

letter=0
digit=0
word=0
m=input('Give a line with word, letter, Digit : ')

for i in m:
    if i>='a' and i<='z':
        letter+=1
    if i>='0' and i<='9':
        digit+=1
    if i==' ':
        word+=1
print(f'word={word}  digit={digit}  letter={letter}')

