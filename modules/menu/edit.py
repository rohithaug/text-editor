#!/usr/bin/env python
'''
__author__ = Rohith S P
__license__ = MIT
__copyright__ = Copyright (c) 2020 Rohith S P
'''

import os
from modules.library import tkinter

class EditMenu:
    def __init__(self, text_area, menu_bar, methods):
        self.text_area = text_area
        self.menu_bar = menu_bar
        self.methods = methods
        self.edit_menu = tkinter.Menu(self.menu_bar, tearoff=0)

        #add Undo, Redo, Cut, Copy and Paste functions to the Edit menu
        self.edit_menu.add_command(label="Undo", command=self.undo, accelerator="Ctrl+Z")
        self.edit_menu.add_command(label="Redo", command=self.redo, accelerator="Ctrl+Y")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=self.cut, accelerator="Ctrl+X")
        self.edit_menu.add_command(label="Copy", command=self.copy, accelerator="Ctrl+C")
        self.edit_menu.add_command(label="Paste", command=self.paste, accelerator="Ctrl+V")
        self.edit_menu.add_command(label="Delete", command=self.delete, accelerator="Del")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Select All\t\t\t\t\t", command=self.select_all, accelerator="Ctrl+A")

        #add Edit menu to menu bar
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        self.assign_functions()

    #function to undo
    def undo(self):
        self.text_area.event_generate("<<Undo>>")

    #function to undo
    def redo(self):
        self.text_area.event_generate("<<Redo>>")

    #function to cut text
    def cut(self):
        self.text_area.event_generate("<<Cut>>")

    #function to copy text
    def copy(self):
        self.text_area.event_generate("<<Copy>>")

    #function to paste text
    def paste(self):
        self.text_area.event_generate("<<Paste>>")

    #function to paste text
    def delete(self):
        self.text_area.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)

    #function to select all text
    def select_all(self):
        self.text_area.event_generate("<<SelectAll>>")

    #save functions to the methods dictionary
    def assign_functions(self):
        self.methods['Undo'] = self.undo
        self.methods['Cut'] = self.cut
        self.methods['Copy'] = self.copy
        self.methods['Paste'] = self.paste
        self.methods['Delete'] = self.delete
        self.methods['SelectAll'] = self.select_all
