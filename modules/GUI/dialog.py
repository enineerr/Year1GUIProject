# import tkinter as tk
from tkinter import ttk
from tkinter import Listbox, StringVar, Toplevel, filedialog, messagebox
from modules.files import files
from json import JSONDecodeError


class dialog:
    def __init__(self) -> None:
        # This is for file handling with the edit menu and maybe also the initial menu
        self.workingFile = None

    def addStudentDialog(self) -> list[str | int] | None:
        dialog = Toplevel(self.root)  # init dialog

        ## Define widgets
        # Buttons
        done = ttk.Button(dialog, text="Done", command=dialog.destroy)
        done.grid(row=10, column=2, padx=5, pady=5, sticky="SE")
        cancel = ttk.Button(dialog, text="Cancel", command=dialog.destroy)
        cancel.grid(row=10, column=1, padx=5, pady=5, sticky="SE")
        ## Labels
        # Name
        nLabel = ttk.Label(dialog, text="Full Name:")
        nLabel.grid(row=0, column=0, padx=5, pady=5, sticky="E")
        # ID
        idLabel = ttk.Label(dialog, text="Student ID:")
        idLabel.grid(row=1, column=0, padx=5, pady=5, sticky="E")
        idSubLabel = ttk.Label(dialog, text="Leave blank to generate new ID")
        idSubLabel["font"] = "TkTooltipFont"
        idSubLabel.grid(row=3, column=1, sticky="NW", columnspan=2, padx=5)

        name = StringVar()
        id = StringVar()

        ## Entries
        # Name
        nEntry = ttk.Entry(dialog, textvariable=name)
        nEntry.grid(row=0, column=1, sticky="NWE", padx=5, pady=5, columnspan=2)
        # SID
        checker = (dialog.register(self.checkID), "%P")
        idEntry = ttk.Entry(dialog, validate="key", textvariable=id, validatecommand=checker)
        idEntry.grid(row=1, column=1, sticky="NWE", padx=5, pady=5, columnspan=2)
        # ID subtext (leave blank for auto) TODO see if entry can just contain this when blank

        dialog.protocol("WM_DELETE_WINDOW", dialog.destroy)  # take over exit
        dialog.transient(self.root)  # set to be dialong rather than main window
        dialog.grab_set()  # prevent input to main window

        # check inputs
        ## TODO consider checking inputs and highlighting the wrong one (ID)
        # dialog.destroy()
        ## TODO change to data struct
        # return None


        # Wait for user to do something
        dialog.wait_window()

        if (id.get() == ""):
            return [str(name.get()).title(), ""]
        return [str(name.get()).title(), int(str(id.get()))]

    @staticmethod
    def checkID(val: str) -> bool:
        # If ID is empty allow
        if (len(val) == 0):
            return True
        # In anything else make sure is a number
        return val.isnumeric()

    def addGrade(self) -> None:
        pass

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
        # self.workingFile = files(filedialog.asksaveasfilename())
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
                self.getFile()
                self.saveFile(True)
