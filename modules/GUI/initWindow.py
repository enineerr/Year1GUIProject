class initWindow:
    def __init__(self) -> None:
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

        self.root.wait()