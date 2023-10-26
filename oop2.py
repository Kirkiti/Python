class Students:
    def __init__(self, name, course, gender, age):
        self.name = name
        self.course = course
        self.gender = gender
        self.age = age

    def display(self):
        print("Name: %s \nCourse: %s \nGender: %s\nAge: %d"
              % (self.name, self.course, self.gender, self.age))


stud1 = Students("Joshua Yator", "Computer Science", "Male", 25)
myobj = Students("Yvonne Barasa", "Bachelor of Commerce", "Female", 21)

stud1.display()
myobj.display()
