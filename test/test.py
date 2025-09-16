import tkinter as tk
from tkinter import ttk
from tkinter import N, E, S, W
from tkinter import Listbox, StringVar, Toplevel





root = tk.Tk()
root.title("Student Grade Manager")

# This is just for demo, dont global a widget..
global dialog
dialog = None


# Dialog
def addStudent():
    dialog = Toplevel(root)  # init dialog

    close = ttk.Button(dialog, text="Close", command=dismiss)
    close.grid(column=10, row=10)

    dialog.protocol("WM_DELETE_WINDOW", dismiss)  # take over exit
    dialog.transient(root)  # set to be dialong rather than main window
    dialog.grab_set()  # prevent input to main window

    dialog.bind("<Return>", dismiss)


def dismiss(key=None):
    dialog.destroy()


# Define main frame everything else is contained within
mainFrame = ttk.Frame(root, padding="2 2 12 12")

# Setup main frame's grid
mainFrame.grid(column=0, row=0, sticky=(N, E, S, W))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
# Set weights for resizing
mainFrame.columnconfigure(0, weight=1)
mainFrame.rowconfigure(0, weight=1)
mainFrame.columnconfigure(1, weight=1)

# Setup Left Frame
LFrame = ttk.Frame(mainFrame)
LFrame.grid(column=0, row=0, sticky=(N, E, S, W))
# Config for listbox
LFrame.columnconfigure(2, weight=1)
LFrame.rowconfigure(1, weight=1)

# Setup right frame
RFrame = ttk.Frame(mainFrame)
RFrame.grid(column=1, row=0, sticky=(N, E, S, W))
# Config for listbox
RFrame.columnconfigure(2, weight=1)
RFrame.rowconfigure(1, weight=1)

# Debug test
# LFrame["relief"] = "sunken"
# LFrame["borderwidth"] = 5
# ttk.Label(LFrame, text="Lframe").grid(column=0, row=0, sticky=(N, W))

# RFrame["relief"] = "sunken"
# RFrame["borderwidth"] = 5
# ttk.Label(RFrame, text="Rframe").grid(column=0, row=0, sticky=(N, E))

## Buttons
# Students
sAddButton = ttk.Button(LFrame, text="Add Student", command=addStudent).grid(row=0, column=0, padx=5, pady=5, sticky=(N, W))
sDelButton = ttk.Button(LFrame, text="Delete Student").grid(row=0, column=1, padx=5, pady=5, sticky=(N, W))
# Grades
gAddButton = ttk.Button(RFrame, text="Add Grade").grid(row=0, column=0, padx=5, pady=5, sticky=(N, W))
gDelButton = ttk.Button(RFrame, text="Delete Grade").grid(row=0, column=1, padx=5, pady=5, sticky=(N, W))

# # Listbox debug
# vals = []
# for values in range(100):
#     vals.append(values)

# valS = StringVar(value=vals)
# valS.set(vals)
# # /Listbox debug

## Listboxes
# L
# LList = Listbox(LFrame, listvariable=valS, selectmode="extended", exportselection=False)
LList = Listbox(LFrame, selectmode="extended", exportselection=False)
LList.grid(row=1, column=0, padx=5, pady=5, columnspan=3, sticky=("NESW"))
# R
# RList = Listbox(RFrame, listvariable=valS, selectmode="extended")
RList = Listbox(RFrame, selectmode="extended")
RList.grid(column=0, row=1, padx=5, pady=5, columnspan=3, sticky=(N, E, S, W))

## Scrollbars
# L
LScroll = ttk.Scrollbar(LFrame)
LScroll.grid(row=1, column=3, sticky="NES", pady=5)
# R
RScroll = ttk.Scrollbar(RFrame)
RScroll.grid(column=3, row=1, sticky=(N, E, S), pady=5)

## Setup scrollbar connections
# L
LScroll.config(command=LList.yview)
LList.config(yscrollcommand=LScroll.set)
# R
RScroll.config(command=RList.yview)
RList.config(yscrollcommand=RScroll.set)


root.mainloop()
