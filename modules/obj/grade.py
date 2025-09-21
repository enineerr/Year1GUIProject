from modules.obj.course import Course


class Grade:
    def __init__(
            self,
            course: Course,
            grade: int = 0
    ) -> None:
        pass

    def __call__(self):
        # make return data
        pass

    def changeGrade(self, newGrade: int) -> None:
        # verify input, if bad raise exception, else change the grade goddamnit
        # verification should be done in a checker file like last assessment
        pass
