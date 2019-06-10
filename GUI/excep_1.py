#exception handling
try:
    a = 5
    b = (int)(input("Enter the divisor = "))
    c=a/b
except Exception as e:
    print(e)
    print("Cannot divide by zero")
    
