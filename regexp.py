import re

# my_string = 'seafood is food, and novel is soul food'
#
# result1 = re.search('foo', my_string)
# result2 = re.findall('foo', my_string)
# result3 = list(re.finditer('foo', my_string))
# print(result1)
# print(result2)
# print(result3.group())

# string2 = 'kiko lives in Tokyo, yukiko lives in Kyoto, and mihoko Otaru'
# pattern = re.compile('ko')
# find_ko = pattern.search(string2)
# result = find_ko.group()
# print(result)

# string3 = 'yukiko mobile number: 1829844794'
# result1 = re.search('.+(\d+)', string3)
# result2 = re.search('.+?(\d+)', string3)
# print(result1.group(1))
# print(result2.group(1))

string4 = 'yukiko phone number: 17711625186, yukiko address: 90-87-55-98C'
re1 = re.findall('kiko', string4)
re2 = re.search('.+(\d+)', string4)
re3 = re.search('(.+?)(\d+)', string4)
#print(re1)
print(re2.group(1))
print(re3.group(1))
print(re3.group(2))
#print(re2.group(2))


