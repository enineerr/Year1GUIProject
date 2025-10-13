from modules.GUI.dialog import dialog


class gradeCB:
    def addGrade(self):
        if (len(self.sSelection) != 1):
            return

        gInfo = dialog(self.sSelection, self.root).addGradeDialog()
        if (gInfo is None):
            return

        # Add grade to the student obj
        self.sSelection[0].addGrade(gInfo[0], gInfo[1])

        self.updateBox1()
        self.updateBox2()

    def editGrade(self):
        # Only work if only 1 selection
        if (len(self.sSelection) != 1):
            return

        name = dialog(self.students, self.root).addStudentDialog(inName=self.sSelection[0].Name, inId=str(self.sSelection[0].ID))
        # Make sure user didnt edit to be blank
        if (name is not None):
            self.sSelection[0].Name = name[0]

        self.updateBox2()

    def delGrade(self, iList=None):
        # Reverse list to prevent indexs from changing after removals if drycall
        if (iList is None):
            iList = list(self.RListSelection)[::-1]

        # index = 0
        # for students in self.sSelection:
        #     for j in students.grades.keys():
        #         if iList[0] == index:
        #             students.removeGrade(j)
        #             iList.pop(0)
        #             if (len(iList) > 0):
        #                 self.delGrade(iList)
        #             return
        if (self.RListSelection == 1):
            # This is awful but its better than alternatives
            self.sSelection.removeGrade(list(self.sSelection.grades.keys())[iList[0]])
        
        self.updateBox2()

    def updateBox2(self) -> None:
        # Clear list var to reinit the whole list at once
        self.gVar = []
        # Clear selection var
        self.sSelection = []

        # Check if new selection is empty
        if (self.LListSelection == ()):
            # If so, set current selection to nothing,
            self.sSelection = []
            # then return
            return

        for i in self.LListSelection:
            # Make sure there are students to show
            if (len(self.students) > 0):
                self.sSelection.append(self.students[i])

        for students in self.sSelection:
            for course, grade in students.grades.items():
                self.gVar.append(f"{course}: {grade}%")
        self.gStrVar.set(self.gVar)
