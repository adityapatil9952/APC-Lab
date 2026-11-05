class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Constructor Called")

    def __del__(self):
        print("Distructor Called")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student("Sanket", 20)

s1.display()

del s1
        