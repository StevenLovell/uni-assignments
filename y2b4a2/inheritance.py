class Person:
    #constructor
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    #class methods
    def showName(self):
        print(self.name)

    def showAge(self):
        print(self.age)

class Student:
    def __init__(self, studentID):
        self.studentID = studentID

        #class methods
    def getID(self):
        print(self.studentID)

class Resident(Person, Student):
    #constructor
    def __init__(self, name, age, studentID):
        Person.__init__(self, name, age)
        Student.__init__(self, studentID)

#main
res1 =Resident("Fred", 25, "2561")
res2 =Resident("Henry",22,"1234")
res1.getID()
res1.showName()
res2.showName()
res2.getID()