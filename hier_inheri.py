#hierarchical inheritance:-------------

class A:
    def fun1(self):
        print("in parent class A")

class B(A):
    def fun2(self):
        print("in child class B")

class C(A):
    def fun3(self):
        print("in child class C")

obj1=B()
obj1.fun1()
obj1.fun2()

obj2=C()
obj2.fun3()

