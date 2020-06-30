#!/usr/bin/env python
'''
__author__ = Rohith S P
__license__ = MIT
__copyright__ = Copyright (c) 2020 Rohith S P
'''

from modules.library import tkinter
from tkinter import *

class ScrollBar:
    def __init__(self, root, text_area):
        self.root = root
        self.text_area = text_area
        self.y_bar()
        self.x_bar()

    def y_bar(self):
        scroll_y = Scrollbar(self.root)

        #add scroll bar
        scroll_y.pack(fill=Y, side=RIGHT)

        #auto adjust scroll bar based on the text height
        scroll_y.config(command=self.text_area.yview)
        self.text_area.config(yscrollcommand=scroll_y.set)

    def x_bar(self):
        scroll_x = Scrollbar(self.root, orient='horizontal')

        #add scroll bar
        scroll_x.pack(fill=X, side=BOTTOM)

        #auto adjust scroll bar based on the text width
        scroll_x.config(command=self.text_area.xview)
        self.text_area.config(xscrollcommand=scroll_x.set)
