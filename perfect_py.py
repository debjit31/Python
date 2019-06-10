#to check if a number is perfect or not
s=0
a=(int)(input("Enter a number = "))
for i in range(1,a):
   if a%i==0:
       s=s+i
if s==a:
   print(a,"is a perfect number ")
else:
   print(a,"is not a perfect number")
