#!/usr/bin/env python
'''
__author__ = Rohith S P
__license__ = MIT
__copyright__ = Copyright (c) 2020 Rohith S P
'''

from modules.library import tkinter
from tkinter import *
from modules.connect_modules import connect

class textarea:
    def __init__(self, root, width=800, height=600):
        self.root = root
        self.text_area = Text(self.root, undo=True, wrap = "none")
        self.width = width
        self.height = height
        self.title()
        self.mondules()
        self.draw()

    def title(self):
        #text editor icon display
        try:
            self.root.iconbitmap("modules\editor.ico")
        except:
            pass

        #text editor title
        self.root.title("untitled - Text Editor")

    def draw(self):

        #text editor geometry
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        left = (screen_width/2) - (self.width/2)
        top = (screen_height/2) - (self.height/2)
        self.root.geometry('{}x{}+{}+{}'.format(self.width, self.height, int(left), int(top)))

        #add text area
        self.text_area.pack(side = "top", expand = True, fill = "both")

        #auto resize text area
        #self.root.grid_rowconfigure(0, weight=1)
        #self.root.grid_columnconfigure(0, weight=1)

    def mondules(self):
        connect(self.root, self.text_area)
        return
