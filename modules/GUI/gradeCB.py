from modules.GUI.dialog import dialog


class gradeCB:
    def addGrade(self):
        if (len(self.sSelection) != 1):
            return

        # Get name and ID
        gInfo = dialog(self.sSelection, self.root).addGradeDialog()
        # Make sure info isnt invalid
        if (gInfo is None):
            return

        # Add grade to the student obj
        self.sSelection[0].addGrade(gInfo[0], gInfo[1])

        self.updateBox1()
        self.updateBox2()

    def editGrade(self):
        # Only work if only 1 selection
        if (len(self.RListSelection) != 1):
            return

        # get info
        gInfo = dialog(self.sSelection, self.root).addGradeDialog(inName=list(self.sSelection[0].grades.keys())[self.RListSelection[0]], inGrade=str(self.sSelection[0].grades[list(self.sSelection[0].grades.keys())[self.RListSelection[0]]]))
        # Make sure user didnt edit to be blank nor cancel
        # if they did, return now.
        if (gInfo is None):
            return
        if (gInfo[0] is None):
            return
        # delete grade
        self.delGrade()
        # add new grade
        self.sSelection[0].addGrade(gInfo[0], gInfo[1])

    def delGrade(self, iList=None):
        # Reverse list to prevent indexs from changing after removals if drycall
        if (iList is None):
            iList = list(self.RListSelection)[::-1]

        # This block manages mapping the two selections to remove a specific grade
        index = 0
        for students in self.sSelection:
            for j in students.grades.keys():
                if iList[0] == index:
                    students.removeGrade(j)
                    iList.pop(0)
                    if (len(iList) > 0):
                        self.delGrade(iList)

                    # Allow quitting
                    self.updateBox2()
                    return
                index += 1

    def updateBox2(self) -> None:
        # Clear list var to reinit the whole list at once
        self.gVar = []
        # Clear selection var
        self.sSelection = []

        # Check if new selection is empty
        if (self.LListSelection == ()):
            # If so, set current selection to nothing,
            self.sSelection = []
            self.gStrVar.set(self.gVar)
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
