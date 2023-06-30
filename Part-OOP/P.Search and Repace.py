import re

pattern = r"colour"

text1 = "red is my favourite colour.also blue colour"

text2 = re.sub(pattern,"color",text1)
# text2 = re.sub(pattern,"color",text1,count=1)

print(text2)
