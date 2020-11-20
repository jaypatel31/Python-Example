class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def getDetails(self):
        print(self.name,"is of age",self.age)

class Student(Person):
    def __init__(self,name, age,id):
        super().__init__(name,age)
        self.id = id
    def getDetails(self):
        print("Name of Student-",self.name)
        print("Age of Student-",self.age)
        print("Roll Number of Student-",self.id)

S1 = Student("Krushang",17,47)

S1.getDetails()
