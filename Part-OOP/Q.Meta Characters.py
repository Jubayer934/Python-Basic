import re

pattern1 = r"^colo.r$"

pattern2 = r"(ab)*"

pattern3= r"(a+b)"

pattern4= r"ice(-)?cream"

pattern5 = r"a{1,3}$"

'''

^=start with colo
.=any character
$=end with r
a*= ony one or nothing will be true
a+= one or more (a) will be true
(a*b)
a+b
a*b*
a+b+

(-)?= (-) is 0 to 1 time

a{1,3}$= 1 to 3 in a string will be true

'''

if re.match(pattern1,"colour"):
    print("Match1")


if re.match(pattern2,"colour"):
    print("Match2")

if re.match(pattern3,"bcolour"):
    print("Match3")

if re.match(pattern3,"colour"):
    print("Match4")

if re.match(pattern4,"icecream"):
    print("Match5")

if re.match(pattern5,"aaa"):
    print("Match6")
