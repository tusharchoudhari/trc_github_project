a=10
class Edureka():
    """
    Explaining number class documenation
    """
    def __init__(self):
        print("Destructor")
        self.__pri=("I am private")
        self._pro="I am protected"
        self.pub="I am public"
        print("This variable can only be accessed within class : {}".format(self.__pri))
    def __del__(self):
        print("Destructor")
        del self
    @classmethod
    def myCustomconstructor(cls,strength):
        cls.strength=strength

if __name__=="__main__":
    x = Edureka()
    y=Edureka.myCustomconstructor('Strong')
    #del x
    a = 20
    print(a)
    #x=Edureka()
    print(x.pub)
    print(x._pro)
    print(x._Edureka__pri)   # private member can't be accessed using object name. But we can access this using this strange syntax.
    print(x)
    print(a)
    print(Edureka.__dict__)
    print(Edureka.__doc__)
    print(Edureka.__name__)
    print(Edureka.__module__)
    print(Edureka.__bases__)
    print("Y={}".format(y.strength))
    #del x
