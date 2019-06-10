try:
    b=(int)(input("Enter a number = "))
    print(b)
    print("End of try block")
##    list1=[1,4,6,2,8]
##    list1[10]=44
except ValueError as e:
    print(e)
except Exception as e1:
    print(e1)
finally:
    print("in the finally block")
        

