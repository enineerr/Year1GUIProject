from pathlib import Path as path
import json
from modules.obj.student import Student


class files:
    def __init__(self, dir) -> None:
        self.workingFile = path(dir)

        if (not path.exists(self.workingFile)):
            with open(self.workingFile, "w"):
                pass

    def saveFile(self, students: list[Student]):
        sDict = {}
        for i in students:
            sDict.update(i())

        with open(self.workingFile, "w") as f:
            f.write(json.dumps(sDict))

    def readFile(self) -> list[Student]:
        with open(self.workingFile, "r") as f:
            data = json.loads(f.read())
        for i in data:
            print(i)