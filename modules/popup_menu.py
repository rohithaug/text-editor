#!/usr/bin/env python
'''
__author__ = Rohith S P
__license__ = MIT
__copyright__ = Copyright (c) 2020 Rohith S P
'''

from modules.library import tkinter

class PopupMenu:
    def __init__(self, root, text_area, methods):
        self.root = root
        self.text_area = text_area
        self.methods = methods

        self.popup_menu = tkinter.Menu(root)
        self.root.bind("<Button-3>", self.do_popup)

        #add Undo, Redo, Cut, Copy and Paste functions to the popup menu
        self.popup_menu.add_command(label="Undo", command=self.methods['Undo'], accelerator="Ctrl+Z")
        self.popup_menu.add_separator()
        self.popup_menu.add_command(label="Cut", command=self.methods['Cut'], accelerator="Ctrl+X")
        self.popup_menu.add_command(label="Copy", command=self.methods['Copy'], accelerator="Ctrl+C")
        self.popup_menu.add_command(label="Paste", command=self.methods['Paste'], accelerator="Ctrl+V")
        self.popup_menu.add_command(label="Delete", command=self.methods['Delete'], accelerator="Del")
        self.popup_menu.add_separator()
        self.popup_menu.add_command(label="Select All\t\t\t\t\t", command=self.methods['SelectAll'], accelerator="Ctrl+A")

    def do_popup(self, event):
         try:
             self.popup_menu.tk_popup(event.x_root, event.y_root)
         finally:
             self.popup_menu.grab_release()
