import re

pattern1 = r"[aeiou]"

pattern2 = r"[a-z][A-Z][0-9]"
'''
any latter at [~~]'''

if re.match(pattern1,"ujubayer"):
    print("Match1")

if re.match(pattern2,"jE1ubayer"):
    print("Match2") 