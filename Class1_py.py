class employee:
    def getdata(self,eid=0,ename="",esal=0):
        self.eid=(int)(input("Enter Employee id :- "))
        self.ename=input("Enter your name = ")
        self.esal=(int)(input("Enter your salaray = "))

    def putdata(self):
        print("Emp id",self.eid)
        print("Emp name",self.ename)
        print("Emp salary",self.esal)

    def total_sal(self,da=0,hra=0):
        self.da=(int)(input("Enter DA = "))
        self.hra=(int)(input("Enter HRA = "))
        t=self.esal+self.da+self.hra
        print("The total salary is ",t)

e1=employee()
e1.getdata()
e1.putdata()
e1.total_sal()






























##class student:
##    def getdata(self,sname="",sroll=0,marks=0):
##        self.sname=input("Enter your name = ")
##        self.sroll=(int)(input("Enter your roll number = "))
##        self.marks=(int)(input("Enter your percentage = "))
##        
##    def print(self):
##        print("Your name is :- ",self.sname)
##        print(self.sname," your roll no. is = ",self.sroll)
##        print("You secured ",self.marks," percenttage of marks")
##        
##obj=student()
##obj.getdata()
##obj.print()






            
                       
        
