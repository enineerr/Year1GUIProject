from tkinter import filedialog, messagebox
from json import JSONDecodeError
from modules.files import files


class fileMan:
    def getFile(self, save: bool = False) -> None:
        file = filedialog.askopenfilename()

        # Make sure something was selected, if not return
        if (file != ()):
            self.workingFile = files(file)
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

        if (file != ()):
            self.workingFile = files(file)
            self.saveFile()

    def saveFile(self) -> None:
        # Check if there is a file yet
        if (self.workingFile is not None):
            # if so try saving to it
            self.workingFile.saveFile(self.students)
        # Otherwise get the file and retry saving
        else:
            # See if the user wants to try again or not.
            if (messagebox.askokcancel("No file selected", "Would you like to choose a file to save to?")):
                self.getFile(True)
                self.saveFile()
