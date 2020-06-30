#!/usr/bin/env python
'''
__author__ = Rohith S P
__license__ = MIT
__copyright__ = Copyright (c) 2020 Rohith S P
'''

import os
from modules.library import tkinter
from tkinter.filedialog import *
from tkinter.messagebox import *

class FileMenu:
    def __init__(self, root, text_area, menu_bar, methods):
        self.root = root
        self.text_area = text_area
        self.menu_bar = menu_bar
        self.file = None
        self.methods = methods
        self.file_menu = tkinter.Menu(self.menu_bar, tearoff=0)

        #add New, Open, Save, Save As and Exit functions to the File menu
        self.file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        self.file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        self.file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        self.file_menu.add_command(label="Save As\t\t\t\t\t", command=self.save_as_file, accelerator="Ctrl+Shift+S")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit, accelerator="Ctrl+Q")

        #add File menu to menu bar
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        #add shortcuts
        self.shortcuts()

    #function to create new file
    def new_file(self, event=None):
        self.file = None
        self.text_area.delete(1.0, END)
        self.root.title("untitled - Text Editor")

    #function to open a file
    def open_file(self, event=None):
        self.file = askopenfilename(defaultextension=".txt", filetypes=[("All files","*.*"), ("Text files", "*.txt")])

        if self.file == "":
            self.file = None
        else:
            self.root.title(os.path.basename(self.file) + " - " + os.path.dirname(self.file) + " - Text Editor")
            self.text_area.delete(1.0, END)
            #read the contents of the file and write it to the text editor
            with open(self.file, "r") as file:
                self.text_area.insert(1.0, file.read())

    #function to save a file
    def save_file(self, event=None):
        #save as new file
        if self.file == None:
            self.file = asksaveasfilename(initialfile="untitled.txt", defaultextension=".txt", filetypes=[("All files","*.*"), ("Text files", "*.txt")])

            if self.file == "":
                self.file = None
            else:
                #write the contents in the notepad to the file
                with open(self.file, "w") as file:
                    file.write(self.text_area.get(1.0, END))

                #update window name
                self.root.title(os.path.basename(self.file) + " - " + os.path.dirname(self.file) + " - Text Editor")

        #write the contents in the notepad to the file and save the file
        else:
            with open(self.file, "w") as file:
                file.write(self.text_area.get(1.0, END))

    #function to save as a file
    def save_as_file(self, event=None):
        if self.file == None:
            self.file = asksaveasfilename(initialfile="untitled.txt", defaultextension=".txt", filetypes=[("All files","*.*"), ("Text files", "*.txt")])

        else:
            self.file = asksaveasfilename(initialfile=self.file, defaultextension=".txt", filetypes=[("All files","*.*"), ("Text files", "*.txt")])

        if self.file == "":
            self.file = None
        else:
            #write the contents in the notepad to the file
            with open(self.file, "w") as file:
                file.write(self.text_area.get(1.0, END))

            #update window name
            self.root.title(os.path.basename(self.file) + " - " + os.path.dirname(self.file) + " - Text Editor")

    #quit the program
    def exit(self, event=None):
        if bool(self.text_area.get(1.0, END).replace('\n','').replace('\t','')):
            if self.file is None:
                save_name = 'untitled.txt'
            else:
                save_name = self.file

            exit_case = askyesnocancel(title='Text Editor',message='Do you want to save the file {} before closing?'.format(save_name))

            if exit_case:
                self.save_file()
                if self.file is None:
                    pass
                else:
                    self.root.destroy()
            elif exit_case == None:
                pass
            else:
                self.root.destroy()
        else:
            self.root.destroy()

    #function to define shortcuts
    def shortcuts(self):
        #new file
        self.root.bind("<Control-n>", self.new_file)
        self.root.bind("<Control-N>", self.new_file)
        #open file
        self.root.bind("<Control-o>", self.open_file)
        self.root.bind("<Control-O>", self.open_file)
        #save file
        self.root.bind("<Control-s>", self.save_file)
        self.root.bind("<Control-S>", self.save_file)
        #save file as
        self.root.bind("<Control-Shift-s>", self.save_as_file)
        self.root.bind("<Control-Shift-S>", self.save_as_file)
        #quit program
        self.root.bind("<Control-q>", self.exit)
        self.root.bind("<Control-Q>", self.exit)
        #save as while close window
        self.root.protocol('WM_DELETE_WINDOW', self.exit)
