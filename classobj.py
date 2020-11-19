class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def getDetails(self):
        print("Student Name - ",self.name)
        print("Student RollNumber - ",self.roll)


S1 = Student("Jay",049)
S1.getDetails()
