#!/usr/bin/env python
'''
__author__ = Rohith S P
__license__ = MIT
__copyright__ = Copyright (c) 2020 Rohith S P
'''

from modules.library import tkinter
from modules.text_area import textarea

class TextEditor:
    def __init__(self, root):
        self.text = tkinter.Text(root)
        textarea(root)

if __name__=='__main__':
    root = tkinter.Tk()
    TextEditor(root)
    root.mainloop()
