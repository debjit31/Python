#to find the sum of the digits of a number
##s=0
##a=(int)(input("Enter a number = "))
##while a>0:
##    r=a%10
##    s=s+r
##    a=a//10
##print(s)

#to check whether a  number is palindrome or not
num=(int)(input("Enter a number = "))
s=0
t=num
while num>0:
    r=num%10
    s=s*10+r
    num=num//10
print("Reverse is = ",s)
if t==s:
    print("Palindrome")
else:
    print("Not Palindrome")



    
