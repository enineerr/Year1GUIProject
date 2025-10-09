import tkinter as tk
from tkinter import ttk
from tkinter import Listbox, StringVar, Toplevel


class Test:
    def __init__(self) -> None:
        # Create root window
        self.root = tk.Tk()
        # Set title
        self.root.title("Student Grade Manager")
        self.mainWindow()

        self.root.mainloop()

    def mainWindow(self) -> None:
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

    def addStudent(self) -> None:
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
        idLabel.grid(row=1, column=0,padx=5, pady=5, sticky="E")
        idSubLabel = ttk.Label(dialog, text="Leave blank to generate new ID")
        idSubLabel["font"] = "TkTooltipFont"
        idSubLabel.grid(row=3, column=1, sticky="NW", columnspan=2, padx=5)

        ## Entries
        # Name
        nEntry = ttk.Entry(dialog)
        nEntry.grid(row=0, column=1, sticky="NWE", padx=5, pady=5, columnspan=2)
        # SID
        idEntry = ttk.Entry(dialog)
        idEntry.grid(row=1, column=1, sticky="NWE", padx=5, pady=5, columnspan=2)
        # ID subtext (leave blank for auto) TODO see if entry can just contain this when blank

        dialog.protocol("WM_DELETE_WINDOW", dialog.destroy)  # take over exit
        dialog.transient(self.root)  # set to be dialong rather than main window
        dialog.grab_set()  # prevent input to main window

        # TODO change to be the done action rather than exit
        # Use lambda because of bind passing the event.
        dialog.bind("<Return>", lambda key: dialog.destroy())

        dialog.wait_window()

    def addGrade(self) -> None:
        dialog = Toplevel(self.root)  # init dialog

        ## Define widgets
        # Buttons
        done = ttk.Button(dialog, text="Done", command=dialog.destroy)
        done.grid(row=10, column=2, padx=5, pady=5, sticky="SE")
        cancel = ttk.Button(dialog, text="Cancel", command=dialog.destroy)
        cancel.grid(row=10, column=1, padx=5, pady=5, sticky="SE")
        ## Labels
        # Name TODO replace with combo box, and have a dialog to add a class
        cLabel = ttk.Label(dialog, text="Class Name:")
        cLabel.grid(row=0, column=0, padx=5, pady=5, sticky="E")
        # ID
        idLabel = ttk.Label(dialog, text="Grade:")
        idLabel.grid(row=1, column=0, padx=5, pady=5, sticky="E")

        ## Entries
        # Name
        nEntry = ttk.Entry(dialog)
        nEntry.grid(row=0, column=1, sticky="NWE", padx=5, pady=5, columnspan=2)
        # SID
        idEntry = ttk.Entry(dialog)
        idEntry.grid(row=1, column=1, sticky="NWE", padx=5, pady=5, columnspan=2)
        # ID subtext (leave blank for auto) TODO see if entry can just contain this when blank

        dialog.protocol("WM_DELETE_WINDOW", dialog.destroy)  # take over exit
        dialog.transient(self.root)  # set to be dialong rather than main window
        dialog.grab_set()  # prevent input to main window

        # TODO change to be the done action rather than exit
        # Use lambda because of bind passing the event.
        dialog.bind("<Return>", lambda key: dialog.destroy())

        dialog.wait_window()


Test()
