#!/usr/bin/env python
'''
__author__ = Rohith S P
__license__ = MIT
__copyright__ = Copyright (c) 2020 Rohith S P
'''

from modules.library import tkinter

class ViewMenu:
    def __init__(self, root, menu_bar):
        self.root = root
        self.menu_bar = menu_bar
        self.view_menu = tkinter.Menu(self.menu_bar, tearoff=0)
        self.full_status = True

        #add Full Screen functions to the View menu
        self.view_menu.add_command(label="Full Screen", command=self.full_screen, accelerator="F11")

        #add View menu to menu bar
        self.menu_bar.add_cascade(label="View", menu=self.view_menu)

        #add shortcuts
        self.shortcuts()

    def full_screen(self, event=None):
        if self.full_status:
            self.root.attributes('-fullscreen', self.full_status)
            self.full_status = False
        else:
            self.root.attributes('-fullscreen', self.full_status)
            self.full_status = True

    #function to define shortcuts
    def shortcuts(self):
        #new file
        self.root.bind("<F11>", self.full_screen)
