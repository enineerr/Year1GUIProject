from tkinter import Tk
from modules.GUI.mainWindow import mainWindow


# This is a wrapper for file naming purposes
class GUI:
    def __init__(self) -> None:
        self.root = Tk()
        mainWindow(self.root)
