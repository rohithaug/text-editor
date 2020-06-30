#!/usr/bin/env python
'''
__author__ = Rohith S P
__license__ = MIT
__copyright__ = Copyright (c) 2020 Rohith S P
'''

import os
from modules.library import tkinter
from tkinter.messagebox import *
from tkinter.font import Font
from webbrowser import open as open_link

class HelpMenu:
    def __init__(self, menu_bar):
        self.menu_bar = menu_bar
        self.help_menu = tkinter.Menu(self.menu_bar, tearoff=0)

        #add About function to the Help menu
        self.help_menu.add_command(label="About Text Editor", command=self.about)
        self.help_menu.add_separator()
        self.help_menu.add_command(label="View License", command=self.view_license)
        self.help_menu.add_command(label="View Source Code", command=self.source_code)

        #add Help menu to menu bar
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

    #about text editor
    def about(self):
        try:
            with open("modules/menu/about.txt", "r", encoding='utf-8') as file:
                about = file.read()
        except:
            about = "Simple Text Editor using Python and tkinter.\n\nCopyright \u00A9 2020 Rohith S P"
            print("\u00A9")

        showinfo("About - Text Editor", about)

    #link to source code
    def source_code(self):
        open_link('https://github.com/rohithaug/')

    #link to source code
    def view_license(self):
        try:
            #read the contents of the license.txt file
            with open("modules\menu\LICENSE.txt", "r") as file:
                license_text_content = "\n     "+file.read().replace('\n','\n     ')

            #create a top level widget
            license_win = tkinter.Toplevel()

            #define window geometry
            license_win.geometry('720x440')

            #create a text and display the contents of the license file
            license_text = tkinter.Text(license_win, font=Font(family="Consolas", size=11))
            license_text.pack(side = "top", expand = True, fill = "both")
            license_win.title("LICENSE - Text Editor")

            #license icon
            try:
                license_win.iconbitmap("modules\menu\license.ico")
            except:
                pass

            license_text.delete(1.0, tkinter.END)

            with open("modules\menu\LICENSE.txt", "r") as file:
                license_text.insert(1.0, license_text_content)

        except:
            open_link('https://github.com/rohithaug/')
