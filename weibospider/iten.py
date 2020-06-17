import re
a = "123abc13;sdas123abc13;sdasds123abc13"
b = re.findall("1..(.*?).3", a)
print(b)
print(len(b))