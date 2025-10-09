import tkinter as tk
from tkinter import ttk
from tkinter import Listbox, StringVar, Toplevel
from modules.GUI.dialog import dialog
from modules.obj.student import Student


class mainWindow(dialog):
    def __init__(self) -> None:
        # This will be the main variable for storing all the ugc in memory
        self.students: list[Student | None] = []

        super().__init__()
        # Create root window
        self.root = tk.Tk()
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

        # Init edit menu
        fileMItem = tk.Menu(menuBar)
        fileMItem.add_command(
            label="Copy",
            command=lambda: self.root.event_generate("<<Copy>>"),
            underline=0
        )
        fileMItem.add_command(
            label="Paste",
            command=lambda: self.root.event_generate("<<Paste>>"),
            underline=0
        )
        menuBar.add_cascade(
            label="Edit",
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
        sDelButton = ttk.Button(LFrame, text="Delete Student")
        sDelButton.grid(row=0, column=1, padx=5, pady=5, sticky="NW")
        sEditButton = ttk.Button(LFrame, text="Edit Student")
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
        LList = Listbox(LFrame, selectmode="extended", exportselection=False)
        LList.grid(row=1, column=0, padx=5, pady=5, columnspan=3, sticky=("NESW"))
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

        self.students.append(Student(sInfo[0], sInfo[1]))
        