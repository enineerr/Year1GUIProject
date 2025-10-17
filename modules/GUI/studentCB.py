from modules.GUI.dialog import dialog
from modules.obj.student import Student


class studentCB:
    def addStudent(self):
        sInfo = dialog(self.students, self.root).addStudentDialog()
        if (sInfo is None):
            return

        largestID = 0

        if sInfo[1] == 0:
            if (len(self.students) == 0):
                largestID = 0
            else:
                for i in self.students:
                    if (i.ID > largestID):
                        largestID = i.ID

            # Add one to make new unique ID
            largestID += 1
            sInfo[1] = largestID

        # Add new student to memory in object form
        self.students.append(Student(sInfo[0], sInfo[1], {}))

        self.updateBox1()

    def editStudent(self):
        # Only work if only 1 selection
        if (len(self.sSelection) != 1):
            return

        name = dialog(self.students, self.root).addStudentDialog(inName=self.sSelection[0].Name, inId=str(self.sSelection[0].ID))
        # Make sure user didnt edit to be blank
        if (name is not None):
            self.sSelection[0].Name = name[0]

        self.updateBox1()

    def delStudent(self):
        for i in self.sSelection:
            self.students.remove(i)
        self.updateBox1()

    def updateBox1(self) -> None:
        # Clear list var to reinit the whole list at once
        self.sVar = []

        # Make there there are students to add to the box
        if (len(self.students) > 0):
            # If so, grab all of them and add names and IDs to LBvar
            for sObj in self.students:
                for IDs, names in sObj().items():
                    # this line grabs the ID's and the names, then concats them to make a single entry
                    self.sVar.append(f"{names[0]} ({IDs})")

        # Update gui list
        self.sStrVar.set(self.sVar)
