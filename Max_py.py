a=(int)(input("Enter the 1st number = "))
b=(int)(input("Enter the 2nd number = "))
c=(int)(input("Enter the 3rd number = "))

if a>b:
    if b>c:
        print(a,"is maximum")
    else:
        print(c,"is maximum")
    
elif b>a:
    if b>c:
        print(b,"is maximum")
    else:
        print(c,"is maximum")
else:
    if b>c:
        print(b,"is maximum")
    else:
        print(c," is maximum")
