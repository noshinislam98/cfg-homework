"""

TASK 2

Write a base class to represent a student. Below is a starter code.
Feel free to add any more new features to your class.
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student
doing a specialization, for example:
Software Student and Data Science student.

"""


class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()


class CFGStudent(Student):

    def __init__(self, name, age, id):
        Student.__init__(self, name, age, id)

    def add_subject(self, subject, grade):
        self.subjects.update({subject: grade})

    def remove_subject(self, subject):
        self.subjects.pop(subject)

    def view_subjects(self):
        for subject, mark in self.subjects.items():
            print(f"Subject: {subject}\tMark: {mark}")


    def overall_mark(self):
        total_marks = 0
        for mark in self.subjects.values():
            total_marks += mark

        number_of_subjects = len(self.subjects)
        return total_marks / number_of_subjects


student = CFGStudent("Noshin", 24, 1)
print(f"Name: {student.name}")
print(f"Age: {student.age}")

student.add_subject("Python", 84)
student.add_subject("SQL", 67)
student.view_subjects()

print(f"The overall mark for {student.name} is {student.overall_mark()}")

student.remove_subject("SQL")
student.view_subjects()
