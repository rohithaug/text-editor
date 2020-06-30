#!/usr/bin/env python
'''
__author__ = Rohith S P
__license__ = MIT
__copyright__ = Copyright (c) 2020 Rohith S P
'''

from modules.scrollbar import ScrollBar
from modules.menubar import MenuBar
from modules.popup_menu import PopupMenu
from modules.statusbar import StatusBar

class connect:
    def __init__(self, root, text_area):
        self.root = root
        self.text_area = text_area
        self.methods = {}
        self.methods['StatusBar'] = True
        self.modules_connections()

    def modules_connections(self):
        StatusBar(self.root, self.text_area)
        ScrollBar(self.root, self.text_area)
        MenuBar(self.root, self.text_area, self.methods)
        PopupMenu(self.root, self.text_area, self.methods)
