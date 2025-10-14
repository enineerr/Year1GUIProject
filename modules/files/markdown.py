from modules.obj.student import Student


class markdown:
    def __init__(self, students: list[Student]) -> None:
        self.students: list[Student] = students

    def genReport(self) -> str:
        # Make sure there are students
        if (len(self.students) < 1):
            return ""

        out = ""
        for i in self.students:
            out += (f"# {i.Name}\n")
            out += (self.genTable(i))
            out += (f"## Final Grade: {self.calcFinal(i)}\n\n")

        return out

    @staticmethod
    def gradeMap(percent: float) -> str:
        if (percent >= 80):
            return "A*"
        elif (percent >= 70):
            return "A"
        elif (percent >= 60):
            return "B*"
        elif (percent >= 50):
            return "B"
        elif (percent >= 40):
            return "C"
        else:
            return "U"

    def genTable(self, stu: Student) -> str:
        """
| Course   | Percent Grade | Letter Grade |
| -------- | ------------- | ------------ |
| Course 1 | 85            | A*           |
| Course 2 | 32            | U            |
| Course 3 | 70            | A            |
        """
        tableStr = ""
        col1: list[str] = []
        col2: list[str] = []
        col3: list[str] = []
        col4: list[str] = []  # Col 4 will only be the rightmost line of the table

        # Get the number of courses plus 2 (for heading and - line) then skeleton columns
        for i in range(len(stu.grades.keys()) + 2):
            col1.append("| ")
            col2.append(" | ")
            col3.append(" | ")
            col4.append(" |")

        # First item is header, second is a placehold for line separator
        courses = ["Course", ""]
        grades = ["Percent Grade", ""]
        letters = ["Letter Grade", ""]

        for c, g in stu.grades.items():
            courses.append(c)
            grades.append(str(g))
            letters.append(self.gradeMap(g))

        cLength = self.getMaxLength(courses)
        gLength = self.getMaxLength(grades)
        lLength = self.getMaxLength(letters)

        # Set horizontal line now
        courses[1] = "-" * cLength
        grades[1] = "-" * gLength
        letters[1] = "-" * lLength

        # Add data to the line vars
        for i in range(len(courses)):
            col1[i] += courses[i].ljust(cLength)
            col2[i] += grades[i].rjust(gLength)
            col3[i] += letters[i].ljust(lLength)

        # Convert from tables to one string
        for i in range(len(col1)):
            tableStr += col1[i] + col2[i] + col3[i] + col4[i] + "\n"

        return tableStr

    def calcFinal(self, stu: Student) -> str:
        grades = list(stu.grades.values())

        # Make sure there are results, otherwise return fail (U)
        if (len(grades) == 0):
            return "U"

        avg = sum(grades) / len(grades)

        return self.gradeMap(avg)

    @staticmethod
    def getMaxLength(l: list) -> int:
        longest = 0
        for i in l:
            iLen = len(str(i))
            if (iLen > longest):
                longest = iLen

        return longest
