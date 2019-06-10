class counter:
    count=0
    def __init__(self):#constructor
        counter.count+=1

    def getcount(self):
        print("The number of objects created is ",counter.count)
    def __del__(self):
        counter.count-=1
c1=counter()#first object
c2=counter()#second object
c3=counter()#third object
c3.getcount()

c1.getcount()
del c1#destructor
c3.getcount()


#hw
#create a class called bank with 3 variables -- name,acno,bal,and
#2 functions for input and display. Also add 2 functions
#more for deposit and withdraw amount respectively
            
