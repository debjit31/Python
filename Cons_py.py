#constructor

class number:

    def __init__(self,a,b):     #constructor definition
        self.a=a
        self.b=b
        
    def disp(self):
        print("1st Number ",self.a)
        print("2nd Number ",self.b)
        
    def total(self):
        return self.a+self.b

a=(int)(input("Enter 1st number = "))
b=(int)(input("Enter 2nd number = "))
num=number(a,b)#constructor called
num.disp()
print("The sum is = ",num.total())
    





























##class Stu:
##    def __init__(self,sname,sroll):
##        self.sname=sname
##        self.sroll=sroll
##        
##    def print(self):
##        print("Your name is :- ",self.sname)
##        print("Your roll no is = ",self.sroll)
##
##sname=input("Enter your name = ")
##sroll=(int)(input("Enter your roll = "))
##s=Stu(sname,sroll)
##s.print()
