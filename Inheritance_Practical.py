# Inheritance (plain Python)
#
# Problem Statement:
# A college has Students. A GradStudent is a Student with an extra course,
# and a ResearchStudent is a GradStudent with an extra research topic.
# Reuse the Student class from Class_Obj_Cons.py (another file in the
# APC lab folder) and extend it using inheritance.
#
# Run:  python Inheritance_Practical.py

import os
import sys

# Get reference of another file in the APC lab folder
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# NOTE: importing runs the demo lines at the bottom of Class_Obj_Cons.py,
# so its output ("Constructor Called" etc.) appears first.
from Class_Obj_Cons import Student


# Single inheritance: GradStudent -> Student
class GradStudent(Student):
    def __init__(self, name, age, course):
        super().__init__(name, age)      # call parent constructor
        self.course = course

    def display(self):                   # method overriding
        super().display()
        print("Course:", self.course)


# Multilevel inheritance: ResearchStudent -> GradStudent -> Student
class ResearchStudent(GradStudent):
    def __init__(self, name, age, course, topic):
        super().__init__(name, age, course)
        self.topic = topic

    def display(self):
        super().display()
        print("Research Topic:", self.topic)


if __name__ == "__main__":
    print("\n--- GradStudent ---")
    g = GradStudent("Riya", 22, "MCA")
    g.display()

    print("\n--- ResearchStudent ---")
    r = ResearchStudent("Aditya", 24, "MSc CS", "Machine Learning")
    r.display()

    print("\nisinstance(r, Student):", isinstance(r, Student))
