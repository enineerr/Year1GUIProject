from modules.obj.grade import Grade


class Student:
    def __init__(
            self,
            fullName: str = "",
            level: int = 0,
            ID: int | None = None
    ) -> None:
        self.name = fullName.title()
        self.level = level
        self.ID = ID
        # self.grades: dict[str, str] = {}
        self.grades: list[Grade] | None = None
