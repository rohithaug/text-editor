#!/usr/bin/env python
'''
__author__ = Rohith S P
__license__ = MIT
__copyright__ = Copyright (c) 2020 Rohith S P
'''

from modules.library import tkinter

from modules.menu.file import FileMenu
from modules.menu.edit import EditMenu
from modules.menu.view import ViewMenu
from modules.menu.help import HelpMenu

class MenuBar:
    def __init__(self, root, text_area, methods):
        self.root = root
        self.text_area = text_area
        self.methods = methods

        self.menu_bar = tkinter.Menu(root)

        FileMenu(self.root, self.text_area, self.menu_bar, self.methods)
        EditMenu(self.text_area, self.menu_bar, self.methods)
        ViewMenu(self.root, self.menu_bar)
        HelpMenu(self.menu_bar)

        self.root.config(menu=self.menu_bar)
