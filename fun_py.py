#functions


##def show():
##    print("hello world!!!!")
##show()
##
##
###function with parameters
##def add(x,y) :
##    print("the sum is = ",(x+y))
##a=(int(input("Enter a number= ")))
##b=(int(input("Enter a number= ")))
##add(a,b)


##def diff(x,y):#function returning a value
##    return x-y
##result=diff(8,2)
##print("the result is ",result)
##
###passing variable numbers  of arguments to a function
##
##def addition(*args):
##    s=0
##    for i in args:
##        s=s+(int)(i)
##    return s
##
##result=addition(2,3,4)
##print("the result is = ",result)
##
##










##result=addition(1,5,6,9)
##print("the result is = ",result)





#how to use keyword arguments in a function

def show(**kwargs):
    for key,value in kwargs.items():
        print(key,"=",value)

show(name="abcd",empid=101,dept="HR")




#lamda functoin

def sqr(n):
    return n*n
print(sqr(5))


#------------------------------lamda function----------------

f=lambda x:x*x
print(f(5))

#lambda is used to create anonymous functions without any name
#and they come with any number of arguments but one single expression


f=lambda x,y,z:x+y+z
print(f(2,3,4))
