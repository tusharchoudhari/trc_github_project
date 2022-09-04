class Base:
    def baseClassMethod(self):
        print("baseClassMethod")

        def fun(self):
            print("baseClassfun")
class Child(Base):
    def fun(self):
        print("childClassfun")
    pass

c=Child()
c.baseClassMethod()
c.fun()