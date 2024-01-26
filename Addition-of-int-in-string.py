import re

string = "asd#100sdh_400sdjh&%300hsjka200_"

s = sum(map(int, re.findall(r'\d+', string)))
l = re.findall(r'\d+', string)

print (l)
print (s)