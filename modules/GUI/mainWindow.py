import tkinter as tk
from tkinter import ttk
from tkinter import Listbox, StringVar
from modules.GUI.dialog import dialog
from modules.obj.student import Student
from modules.GUI.fileMan import fileMan
from modules.GUI.studentCB import studentCB
from modules.GUI.gradeCB import gradeCB


class mainWindow(fileMan, studentCB, gradeCB):
    def __init__(self) -> None:
        # This will be the main variable for storing all the ugc in memory
        self.students: list[Student] = []

        # Left box selection but referenced using student objects from main list
        self.sSelection: list[Student] = []

        # Allow remembering the selection so box2 can be updated by grade a/e/d functions
        self.LListSelection = ()
        # Where as this is just for consistency
        self.RListSelection = ()

        super().__init__()
        # Create root window
        self.root = tk.Tk()

        # Prepare LListBox (student) variable
        self.sVar = []
        self.sStrVar = StringVar(value=self.sVar)

        # Prepare RListBox (grades) variable
        self.gVar = []
        self.gStrVar = StringVar(value=self.gVar)

        # Init working file var
        self.workingFile = None

        # Set Title
        self.root.title("Student Grade Manager")

        # Paint mainWindow
        self.mainWindow()

        # Start initDialog
        fChoice = dialog(self.students, self.root).initDialog()

        match fChoice:
            case 0: return
            case 1: self.getFile()
            case 2: self.saveAs()

        # Start mainloop
        self.root.mainloop()

        if (self.workingFile is not None):
            self.saveFile()
        else:
            self.saveAs()

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
        gDelButton = ttk.Button(RFrame, text="Delete Grade", command=self.delGrade)
        gDelButton.grid(row=0, column=1, padx=5, pady=5, sticky="NW")
        gEditButton = ttk.Button(RFrame, text="Edit Grade", command=self.editGrade)
        gEditButton.grid(row=0, column=2, padx=5, pady=5, sticky="NW")
        # Gen grades
        gGenButton = ttk.Button(RFrame, text="Generate Report", command=self.saveReport)
        gGenButton.grid(row=2, column=2, sticky="SE", columnspan=2)
        gGenButton["padding"] = (5, 0, 5, 5)

        ## Listboxes
        # L
        LList = Listbox(LFrame, selectmode="extended", exportselection=False, listvariable=self.sStrVar)
        LList.grid(row=1, column=0, padx=5, pady=5, columnspan=3, sticky=("NESW"))
        LList.bind("<<ListboxSelect>>", lambda _: self.sUpdateSelection(LList.curselection()))
        # R
        RList = Listbox(RFrame, selectmode="extended", exportselection=False, listvariable=self.gStrVar)
        RList.grid(column=0, row=1, padx=5, pady=5, columnspan=3, sticky="NESW")
        RList.bind("<<ListboxSelect>>", lambda _: self.gUpdateSelection(RList.curselection()))

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

    def sUpdateSelection(self, selection):
        self.LListSelection = selection
        self.updateBox2()

    def gUpdateSelection(self, selection):
        self.RListSelection = selection
