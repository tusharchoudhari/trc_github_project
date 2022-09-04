class Edureka:
    def __init__(self,courseName):
        self.courseName=courseName.upper()
    def getCourseName(self):
        return self.courseName
    def setCourseName(self,courseName):
        self.courseName=courseName.upper()
ob=Edureka("Python")
print(ob.getCourseName())
ob.setCourseName("Machine Learning")
print(ob.getCourseName())

