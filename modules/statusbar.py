#!/usr/bin/env python
'''
__author__ = Rohith S P
__license__ = MIT
__copyright__ = Copyright (c) 2020 Rohith S P
'''

from modules.library import tkinter
from tkinter import *

class StatusBar:
    def __init__(self, root, text_area, status=1):
        self.root = root
        self.text_area = text_area
        self.status = status
        self.statusbar = Label(root, text="\tCopyright \u00A9 2020 Rohith S P"+"\t"*9+"Line: 1 | Column: 1\t", bd=1, relief=SUNKEN, anchor=W)
        self.statusbar.pack(side=BOTTOM, fill=X)
        self.shortcuts()

    def update_cursor_info(self, event=None):
        line, column = self.text_area.index(INSERT).split('.')
        line_num, column_num = str(int(line)), str(int(column)+1)
        infotext = "\tCopyright \u00A9 2020 Rohith S P"+"\t"*9+"Line: {} | Column: {}\t".format(line_num, column_num)
        self.statusbar.configure(text=infotext)

    def show_cursor_status(self):
        if self.status == 1:
            self.cursorbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        else:
            self.cursorbar.pack_forget()

    #function to define shortcuts
    def shortcuts(self):
        self.root.bind('<Any-KeyPress>', self.update_cursor_info)
        self.root.bind('<Button-1>', self.update_cursor_info)
