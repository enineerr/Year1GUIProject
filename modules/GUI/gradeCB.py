class gradeCB:
    def updateBox2(self, selection) -> None:
        # Clear list var to reinit the whole list at once
        self.gVar = []
        # Clear selection var
        self.sSelection = []

        # Check if new selection is empty
        if (selection == ()):
            # If so, set current selection to nothing,
            self.sSelection = []
            # then return
            return

        for i in selection:
            # Make sure there are students to show
            if (len(self.students) > 0):
                self.sSelection.append(self.students[i])
