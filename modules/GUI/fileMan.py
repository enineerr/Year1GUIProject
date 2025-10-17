from tkinter import filedialog, messagebox
from json import JSONDecodeError
from modules.files import files, markdown


class fileMan:
    def getFile(self, save: bool = False) -> None:
        file = filedialog.askopenfilename()

        # Make sure something was selected, if not return
        if ((file != ()) or file != "."):
            self.workingFile = files(file)
            # If save is true, file will be overwritten, therefore do not try to read.
            if (not save):
                try:
                    self.students = self.workingFile.readFile()
                except JSONDecodeError:
                    messagebox.showerror(
                        "Data unreadable",
                        "The file selected did not contain valid JSON"
                    )
                self.updateBox1()

    def saveAs(self) -> None:
        file = filedialog.asksaveasfilename()

        # () is returned on cancel on unix
        # "." is returned on NT
        # thanks tkinter
        if ((file != ()) or file != "."):
            self.workingFile = files(file)
            self.saveFile()

    def saveFile(self) -> None:
        # Check if there is a file yet
        if (self.workingFile is not None):
            # Hard fix for tkinter windows implementation of filedialogs being completely different and returning local directory when cancelled???
            if (str(self.workingFile.workingFile) == "."):
                self.workingFile = None
                self.saveFile()
            else:
                # if so try saving to it
                self.workingFile.saveFile(self.students)
        # Otherwise get the file and retry saving
        else:
            # See if the user wants to try again or not.
            if (messagebox.askokcancel("No file selected", "Would you like to choose a file to save to?")):
                self.getFile(True)
                self.saveFile()

    def saveReport(self):
        file = filedialog.asksaveasfilename()

        # () is returned on cancel on unix
        # "." is returned on NT
        # thanks tkinter
        if ((file != ()) or file != "."):
            with open(file, "w") as f:
                # Report all students if none are selected
                if (len(self.sSelection) == 0):
                    f.write(markdown.markdown(self.students).genReport())
                else:
                    f.write(markdown.markdown(self.sSelection).genReport())
