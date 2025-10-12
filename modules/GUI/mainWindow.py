import tkinter as tk
from tkinter import ttk
from tkinter import Listbox, StringVar, Toplevel
from modules.GUI.dialog import dialog
from modules.obj.student import Student


class mainWindow(dialog):
    def __init__(self) -> None:
        # This will be the main variable for storing all the ugc in memory
        self.students: list[Student] = []

        self.sSelection: list[Student] = []

        super().__init__()
        # Create root window
        self.root = tk.Tk()

        # Prepare LListBox (student) variable
        self.sVar = []
        self.sStrVar = StringVar(value=self.sVar)

        # Prepare RListBox (grades) variable
        self.gVar = []
        self.gStrVar = StringVar(value=self.gVar)

        # Set Title
        self.root.title("Student Grade Manager")

        # Paint mainWindow
        self.mainWindow()

        # Start mainloop
        self.root.mainloop()

    def mainWindow(self) -> None:
        # Init menubar
        menuBar = tk.Menu(self.root)
        self.root.config(menu=menuBar)

        # Init file menu
        fileMItem = tk.Menu(menuBar)
        fileMItem.add_command(
            label="Open",
            command=self.getFile
        )
        fileMItem.add_command(
            label="Save",
            command=self.saveFile
        )
        fileMItem.add_command(
            label="Save As",
            command=self.saveAs
        )
        menuBar.add_cascade(
            label="File",
            menu=fileMItem,
            underline=0
        )

        # Define main frame everything else is contained within
        mainFrame = ttk.Frame(self.root, padding="2 2 12 12")

        # Setup main frame's grid
        mainFrame.grid(column=0, row=0, sticky="NESW")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        # Set weights for resizing
        mainFrame.columnconfigure(0, weight=1)
        mainFrame.rowconfigure(0, weight=1)
        mainFrame.columnconfigure(1, weight=1)

        # Setup Left Frame
        LFrame = ttk.Frame(mainFrame)
        LFrame.grid(column=0, row=0, sticky="NESW")
        # Config for listbox
        LFrame.columnconfigure(2, weight=1)
        LFrame.rowconfigure(1, weight=1)

        # Setup right frame
        RFrame = ttk.Frame(mainFrame)
        RFrame.grid(column=1, row=0, sticky="NESW")
        # Config for listbox
        RFrame.columnconfigure(2, weight=1)
        RFrame.rowconfigure(1, weight=1)

        ## Buttons
        # Students
        sAddButton = ttk.Button(LFrame, text="Add Student", command=self.addStudent)
        sAddButton.grid(row=0, column=0, padx=5, pady=5, sticky="NW")
        sDelButton = ttk.Button(LFrame, text="Delete Student", command=self.delStudent)
        sDelButton.grid(row=0, column=1, padx=5, pady=5, sticky="NW")
        sEditButton = ttk.Button(LFrame, text="Edit Student", command=self.editStudent)
        sEditButton.grid(row=0, column=2, padx=5, pady=5, sticky="NW")
        # Grades
        gAddButton = ttk.Button(RFrame, text="Add Grade", command=self.addGrade)
        gAddButton.grid(row=0, column=0, padx=5, pady=5, sticky="NW")
        gDelButton = ttk.Button(RFrame, text="Delete Grade")
        gDelButton.grid(row=0, column=1, padx=5, pady=5, sticky="NW")
        gEditButton = ttk.Button(RFrame, text="Edit Grade")
        gEditButton.grid(row=0, column=2, padx=5, pady=5, sticky="NW")
        # Gen grades
        gGenButton = ttk.Button(RFrame, text="Generate Report")
        gGenButton.grid(row=2, column=2, sticky="SE", columnspan=2)
        gGenButton["padding"] = (5, 0, 5, 5)

        ## Listboxes
        # L
        # LList = Listbox(LFrame, listvariable=valS, selectmode="extended", exportselection=False)
        LList = Listbox(LFrame, selectmode="extended", exportselection=False, listvariable=self.sStrVar)
        LList.grid(row=1, column=0, padx=5, pady=5, columnspan=3, sticky=("NESW"))
        LList.bind("<<ListboxSelect>>", lambda _: self.updateBox2(LList.curselection()))
        # R
        # RList = Listbox(RFrame, listvariable=valS, selectmode="extended")
        RList = Listbox(RFrame, selectmode="extended")
        RList.grid(column=0, row=1, padx=5, pady=5, columnspan=3, sticky="NESW")

        ## Scrollbars
        # L
        LScroll = ttk.Scrollbar(LFrame)
        LScroll.grid(row=1, column=3, sticky="NES", pady=5)
        # R
        RScroll = ttk.Scrollbar(RFrame)
        RScroll.grid(column=3, row=1, sticky="NES", pady=5)

        ## Setup scrollbar connections
        # L
        LScroll.config(command=LList.yview)
        LList.config(yscrollcommand=LScroll.set)
        # R
        RScroll.config(command=RList.yview)
        RList.config(yscrollcommand=RScroll.set)

    def addStudent(self):
        sInfo = self.addStudentDialog()
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
        self.students.append(Student(sInfo[0], sInfo[1]))

        self.updateBox1()

    def editStudent(self):
        # Only work if only 1 selection
        if (len(self.sSelection) != 1):
            return

        name = self.addStudentDialog(inName=self.sSelection[0].Name, inId=str(self.sSelection[0].ID))
        # Make sure user didnt edit to be blank
        if (name is not None):
            self.sSelection[0].name = name[0]

        self.updateBox1()

    def delStudent(self):
        for i in self.sSelection:
            self.students.remove(i)
        self.updateBox1()

    def updateBox1(self) -> None:
        # Clear list var to reinit the whole list at once
        self.sVar = []

        if (len(self.students) > 0):
            for sObj in self.students:
                for IDs, names in sObj().items():
                    # this line grabs the ID's and the names, then concats them to make a single entry
                    self.sVar.append(f"{names[0]} ({IDs})")

        # Update gui list
        self.sStrVar.set(self.sVar)

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
