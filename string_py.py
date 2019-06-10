#string

s="hello"
print(s[0])

for i in range(len(s)):
    print(s[i],end=' ')
print()

for c in s:
    print(c,end=' ')
print()

w="world"
r=s+w# string concatenation
print(r)


if s==w:# string comparison
    print("identical")
else:
    print("not identical")


s="a"
print(s.isalpha())
print(s.isdigit())
s="today is thursday"
print(s.capitalize())
print(s.upper())
s="HELLO"
print(s.lower())

print(s.startswith("H"))
print(s.endswith("O"))



s="TODAY IS THURSDAY"
print(s.replace("TODAY","TOMORROW"))

#s[1]="A"#not supported

print(s[2:4])#prints all characters between index 2 and 3(slicing of string)
















