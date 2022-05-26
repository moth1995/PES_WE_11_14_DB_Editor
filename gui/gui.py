from tkinter import Button, Entry, Label, Listbox, Menu, Scrollbar, Spinbox, TclError, Tk, filedialog, messagebox

class Gui:
    appname='AFL File Editor'
    
    def __init__(self, master:Tk):
        """
        Class constructor

        Args:
            master (Tk): The master object Tk represents the heritage of the whole class.
        """
        self.master = master
        master.title(self.appname)
        w = 600 # width for the Tk root
        h = 530 # height for the Tk root
        # get screen width and height
        ws = master.winfo_screenwidth() # width of the screen
        hs = master.winfo_screenheight() # height of the screen
        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        # set the dimensions of the screen 
        # and where it is placed
        master.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.my_menu=Menu(self.master)
        master.config(menu=self.my_menu)
        self.file_menu = Menu(self.my_menu, tearoff=0)
        self.edit_menu = Menu(self.my_menu, tearoff=0)
        self.help_menu = Menu(self.my_menu, tearoff=0)

        self.my_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open)
        self.file_menu.add_command(label="Save", state='disabled',command=self.save_btn_action)
        self.file_menu.add_command(label="Save as...", state='disabled', command=self.save_as_btn_action)
        self.file_menu.add_command(label="Exit", command=self.master.quit)

        self.my_menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Create AFL from AFS", command=self.create_afl_from_afs)
        self.edit_menu.add_command(label="Export to CSV", state='disabled', command=self.export_to_csv)
        self.edit_menu.add_command(label="Import from CSV", state='disabled', command=self.import_from_csv)

        self.my_menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="Manual", command=self.manual)
        self.help_menu.add_command(label="About", command=self.about)

        self.files_lbl = Label(self.master, text="File list")
        self.files_lbx = Listbox(self.master, height = 31, width = 50, exportselection=False)
        self.files_sb = Scrollbar(self.master, orient="vertical") 
        self.files_sb.config(command = self.files_lbx.yview)
        self.files_lbx.config(yscrollcommand = self.files_sb.set)
        self.files_lbx.bind('<<ListboxSelect>>',lambda event: self.on_file_selected())
        self.file_name_lbl = Label(self.master,text="New file name")
        self.file_box = Entry(self.master, width=32, state='disabled')
        self.apply_btn = Button(self.master, text="Apply", state='disabled', command=self.on_apply_btn_click)
        self.clear_btn = Button(self.master, text="Clear", state='disabled', command=self.on_clear_btn_click)
        self.quantity_of_files = Spinbox(self.master, width=5,from_=1, to=256, state='disabled')
        self.add_more_btn = Button(self.master, text="Add more files", command=self.on_add_more_files_btn_click, state='disabled')
        self.publish()

    def publish(self):
        """
        Method to expose the gui into the form
        """

        self.files_lbl.place(x=20, y=5)
        self.files_sb.place(x=303.5, y=30, height=500)
        self.files_lbx.place(x=0, y=30)
        
        self.file_name_lbl.place(x=350, y=30)
        self.file_box.place(x=350, y=60)
        self.apply_btn.place(x=400, y=90)
        self.clear_btn.place(x=460, y=90)

        self.quantity_of_files.place(x=420, y=150)
        self.add_more_btn.place(x=400, y=190)
        
    def on_add_more_files_btn_click(self):
        """
        Action to add more files into the afl file and the listbox
        """
        files_to_add = int(self.quantity_of_files.get())
        if not (0 < files_to_add <= 256):
            messagebox.showerror(title=self.appname,message=f"The numbers of files to add must be between 0 and 256")
            return 0
        self.afl_file.add_file(files_to_add)
        self.reload_gui_items()
        
    def on_file_selected(self):
        """
        Action to load the selected file text from the listbox into the entry text widget.
        """
        if self.files_lbx.size() == 0:
            return 0
        # set the name to the entry box
        self.file_box.delete(0,'end')
        self.file_box.insert(0,self.files_lbx.get(self.files_lbx.curselection()))

    def on_apply_btn_click(self):
        """
        Handler to clic event on apply button
        """
        try:
            file_idx = self.files_lbx.get(0, "end").index(self.files_lbx.get(self.files_lbx.curselection()))
            self.afl_file.set_name(file_idx,self.file_box.get())
            self.reload_gui_items(file_idx)
        except TclError as e:
            messagebox.showerror(title=self.appname, message=f'You must select one item before clic here \n{e}')

    def on_clear_btn_click(self):
        """
        Handler to clic event on clear button
        """
        self.file_box.delete(0,'end')
        self.files_lbx.selection_clear(0, 'end')

    def open(self):
        """
        Shows the user an interactive menu to select their afl file and then update the whole gui
        enabling widgets

        Returns:
            Bolean: Returns False if the user hits the "cancel" button, otherwise does their actions
        """
        filetypes = [
            ('AFÑ files', '*.AFL'),
            ('All files', '*.*')
        ]

        filename = filedialog.askopenfilename(
            title=f'{self.appname} Open a AFL file',
            initialdir='.',
            filetypes=filetypes)
        if filename == "":
            return 0
        # do something with the file
        self.reload_gui_items()

    def reload_gui_items(self,item_idx = None):
        """
        Refresh the whole gui once there's an update in one of the elements such as a new afl file or any file name change, etc

        Args:
            item_idx (int, optional): optional parameter, in case you need to keep the current selection on the listbox after the update
        """
        self.file_menu.entryconfig("Save", state="normal")
        self.file_menu.entryconfig("Save as...", state="normal")
        self.edit_menu.entryconfig("Export to CSV", state="normal")
        self.edit_menu.entryconfig("Import from CSV", state="normal")
        self.files_lbx.delete(0,'end')
        self.files_lbx.insert('end',*self.afl_file.files)
        self.file_box.config(state='normal')
        self.apply_btn.config(state='normal')
        self.clear_btn.config(state='normal')
        self.quantity_of_files.config(state='normal')
        self.add_more_btn.config(state='normal')
        if item_idx!=None:
            # After we clic on the button we lost the item selection so with this we solve it
            self.files_lbx.select_set(item_idx)

    def save_btn_action(self):
        try:
            #call the object method save_file
            #object.save_file()
            messagebox.showinfo(title=self.appname,message=f"All changes saved at {self.object.file_location}")
        except EnvironmentError as e: # parent of IOError, OSError *and* WindowsError where available
            messagebox.showerror(title=self.appname,message=f"Error while saving, error type={e}, try running as admin")

    def save_as_btn_action(self):
        try:
            new_location = filedialog.asksaveasfile(initialdir=".",title=self.appname, mode='wb', filetypes=([("All files", "*")]), defaultextension=f".{self.object.file_extension}")
            if new_location is None:
                return 0
            self.object.save_file(new_location.name)
            messagebox.showinfo(title=self.appname,message=f"All changes saved at {self.object.file_location}")
        except EnvironmentError as e: # parent of IOError, OSError *and* WindowsError where available
            messagebox.showerror(title=self.appname,message=f"Error while saving, error type={e}, try running as admin or saving into another location")


    def about(self):
        messagebox.showinfo(title=self.appname,message=
        """
        Say thanks to the people who helped you to made this possible or just say thanks to yourself and tell others
        how amazing you're, also its useful to put here your changelog
        """.replace('        ', ''))

    def manual(self):
        messagebox.showinfo(title=self.appname,message=
        r"""
        Write here some manual to your tool
        """.replace('        ', ''))

    def start(self):
        self.master.resizable(False, False)
        self.master.mainloop()

