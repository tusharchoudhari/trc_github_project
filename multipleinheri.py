class A:
    def __init__(self):
        super(A, self).__init__()
        print("method A")


class B:
    def __init__(self):
        super(B, self).__init__()
        print("method B")
class C(A,B):
    def __init__(self):
        super(C,self).__init__()
        print("method C")
    def myMethod(self):
        print("Parent method")
class D(C):
    def __init__(self):
        super(D,self).__init__()
        print("method D")
    def myMethod(self):
        print("Child method")

d=D()
#d.super().myMethod()

"""
c.method()
c.methodB()
c.methodA()
d=D()
d.methodD()
"""
