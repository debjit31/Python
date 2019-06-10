##n1 = (int)(input("Enter a starting number = "))
##n2 = (int)(input("Enter a ending number = "))
##i = n1
##while i <= n2:
##    if i%7==0 and i%5 != 0:
##        print(i,end=" ")
##    i = i+1

import math

a = (int)(input("Enter the value of a = "))
b = (int)(input("Enter the value of b = "))
c = (int)(input("Enter the value of c = "))
if a == 0 and b == 0:
    print("No Solution")
elif a == 0 and b != 0:
    print("Linear Equation")
    root = -c/b
    print("Root = ",root)
else:
    D = b*b-4*a*c
    if D>0:
        print("Roots are real")
        rt = -b+math.sqrt(D*2*a)
        rt1 = -b-math.sqrt(D*2*a)
        print("The roots are = ",rt,rt1)
    else:
        print("The roots are the complex conjugate of each other.")
        rt_1 =-b*2*a+math.sqrt(-2*a*D)
        rt_2 =-b*2*a-math.sqrt(-2*a*D)
        print("The roots are = ",rt_1,"i","  ",rt_2,"i")
