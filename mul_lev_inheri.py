class A:
    def show(self):
        print("in parent class")

class B(A): #B is the child of A
    def disp(self):
        print("in child class")

class C(B):
    def put(self):
        print("in 2nd child class")
        

obj=C()
obj.show()
obj.disp()
obj.put()
