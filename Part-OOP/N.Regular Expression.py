import re

pattern1 = r"jubayer"
pattern2 = r"is"

if re.match(pattern1,"jubayer is a good boy,is he not?"):
    print("Match")

if re.match(pattern2,"jubayer is a good boy, is he not?"):
    print("match")

else :
    print("Not match")



if re.search(pattern1,"jubayer is a good boy,is he not?"):
    print("Match")

if re.search(pattern2,"jubayer is a good boy, is he not?"):
    print("match")

else :
    print("Not match")


print(re.findall(pattern1,"jubayer is a good boy, is he not?"))
print(re.findall(pattern2,"jubayer is a good boy, is he not?"))

