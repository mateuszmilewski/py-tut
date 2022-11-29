import re

str = 'this is a test sentence'

result = re.findall("t..t", str)
print(result)
result = re.findall("t...", str)
print(result)
result = re.findall("\bt", str)
print(result)