class Bank:
    
    def getdata(self,name="",acno=0,bal=0):
        self.name=input("Enter your name :- ")
        self.acno=(int)(input("Enter your account number = "))
        self.bal=1000
    def display(self):
        print("Your name is :- ",self.name)
        print("Your account number is = ",self.acno)
        print("Your balance = ",self.bal)

    def withdraw(self,wid=0):
        self.wid=(int)(input("Enter your withdraw amount = "))
        self.bal=self.bal-self.wid
        if self.bal<0:
            self.bal=0
            print("Your balance after withdrawal  is = ",self.bal)
        else:
            print("Your balance after withdrawal  is = ",self.bal)

    def deposit(self,dep=0):
        self.dep=(int)(input("Enter your deposit amount = "))
        self.bal=self.bal+self.dep
        if self.bal<0:
            self.bal=0
            print("Your balance = ",self.bal)
        else:
              print("Your balance = ",self.bal)
    
obj=Bank()
obj.getdata()
obj.display()
obj.withdraw()
obj.deposit()
