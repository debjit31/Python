name=input("Enter the name of the student....")
num1=(int)(input("Enter the marks of 1st Subject = "))
num2=(int)(input("Enter the marks of 2nd Subject = "))
num3=(int)(input("Enter the marks of 3rd Subject = "))
c=(num1+num2+num3)/3
print("Average marks is = ","%.2f"%(c))
if c<50:
    print("Grade - Fail")
elif c>=50 and c<=59:
    print("Grade-Fair")
elif c>=60 and c<=69:
    print("Grade Good")
elif c>=70 and c<=79:
    print("Grade-Very Good")
else:
    print("Grade Excellent")
