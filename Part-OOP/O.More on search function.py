import re

pattern = r"colour"

text = "red is my favourite colour"

match= re.search(pattern,text)

print(match)
if match:
    print(match.start())
    print(match.end())
    print(match.span())