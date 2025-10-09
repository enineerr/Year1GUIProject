import json


class Student:
    def __init__(self, name: str, ID: int) -> None:
        self.ID = 789
        self.Name = "NameEr"
        self.grades = []

    def __call__(self):
        grades = []
        for i in self.grades:
            grades.append(i())
        return {self.Name: [self.ID, grades]}

    def addGrade(self, courseName: str, grade: float):
        self.grades.append(Grade(courseName, grade))


class Grade:
    def __init__(self, courseName: str, grade: float) -> None:
        self.course = courseName
        self.grade = grade

    def __call__(self):
        return [self.course, self.grade]



# s = Student()
# print(json.dumps(s()))

s1 = Student("User", 1)
s1.addGrade("Computer science", 92.3)
s1.addGrade("Networking", 80.2)
print(json.dumps(s1()))