class Student:
    main_arr = list()
    current = 0
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.main_arr.append(name)

    def getDetails(self):
        print("Student Name - ",self.name)
        print("Student RollNumber - ",self.roll)

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current < len(self.main_arr):
            item = self.main_arr[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration


S1 = Student("Jay",49)
S1 = Student("Ajay",59)
S1 = Student("Ketul",99)
itr = iter(S1)
for name in itr:
    print("Student Name :",name)
