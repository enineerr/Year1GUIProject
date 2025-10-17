class Student:
    def __init__(
            self,
            name: str,
            ID: int,
            grades: dict[str, float] = {}
    ) -> None:
        self.ID = ID
        self.Name = name.title()
        self.grades = grades

    def __call__(self):
        # this can then be combined with the other dictionaries using .update()
        return {self.ID: [self.Name, self.grades]}

    def addGrade(self, courseName: str, grade: float):
        self.grades[courseName.title()] = grade

    def removeGrade(self, key):
        del self.grades[key]
