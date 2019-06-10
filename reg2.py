import re
out = re.search('Deep','Deep Deepak Saha')

print(out.group())
#match fuction will look for the pattern in the beginning of the string
#string
#search function will look for the pattern anywhere in the string
#findall function will return a list if the pattern matches the string
f = re.findall('Webtek','Webtek Labs....We are at Webtek ')
print(f)
