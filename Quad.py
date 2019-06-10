a=(int)(input("Enter the value of a = "))
b=(int)(input("Enter the value of b = "))
c=(int)(input("Enter the value of c = "))
D = b*b - 4*a*c
if a == 0 and b == 0:
    print("No Solution")
elif a == 0 and b != 0:
    print("Linear Solution!!!!")
    r=-c//b
    print("The root of the equation is = ",r)
#print("The discrimant = ",D)
elif D > 0:
    print("The discrimant = ",D)
    print("Real roots!!!!")
    d1 = -b+sqrt(D*2*a);
    d2 = -b-sqrt(D*2*a);
    print("The roots are = ",d1,d2)
    
    
 
