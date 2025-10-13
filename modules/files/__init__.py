from pathlib import Path as path
import json
from modules.obj.student import Student


class files:
    def __init__(self, dir) -> None:
        self.workingFile = path(dir)

        if (not path.exists(self.workingFile)):
            if (not path.is_dir(self.workingFile)):
                with open(self.workingFile, "w"):
                    return

    def saveFile(self, students: list[Student]):
        sDict = {}
        for i in students:
            sDict.update(i())

        with open(self.workingFile, "w") as f:
            f.write(json.dumps(sDict))

    def readFile(self) -> list[Student]:
        with open(self.workingFile, "r") as f:
            data: dict[int, list[str | dict[str, float]]] = json.loads(f.read())

            out = []
            for IDs, info in data.items():
                out.append(
                    Student(
                        name=info[0],
                        ID=int(IDs),
                        grades=info[1]
                    )
                )

            return out