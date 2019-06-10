#multiple inheritance:------------


class student:
    def getdata(self,roll=0,name=""):
        self.roll=roll
        self.name=name

    def putdata(self):
        print("roll",self.roll)
        print("name ",self.name)

class marks:
    def getmarks(self,m1=0,m2=0):
        self.m1=m1
        self.m2=m2

    def putmarks(self):
        print("marks in 1st subject",self.m1)
        print("marks in 2nd subject",self.m2)


class result(student,marks):
    def gettotal(self):
        return self.m1+self.m2


r=result()
r.getdata(1,"abc")
r.getmarks(50,70)
r.putdata()
r.putmarks()
print("the total marks is ",r.gettotal())
