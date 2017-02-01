##  Python: 3.6.0
##
##  Author: Christopher Garrick
##
##  Purpose:  The Tech Academy - Python Course, Item 65
##            PyDrill_gui_34_idle
##            Create a GUI for a program that will transfer files updated
##            within the last 24 hours.

import os
import shutil as stl
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import datetime as dt
from os.path import getmtime
from datetime import datetime
from datetime import timedelta
from tkinter.filedialog import askdirectory
import re
import PyDrill_main
import PyDrill_gui
from PyDrill_gui import *


filenamea = ''
filenameb = ''


def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


def ask_quit(self):
    if messagebox.askokcancel('Exit program', 'okay to exit application?'):
        self.master.destroy()
        os._exit(0)
        

def findFile1(self):
    filenamea = askdirectory()
    filenamea = re.sub('/', r'\\', filenamea)
    print(filenamea)
    return filenamea


def findFile2(self):
    filenameb = askdirectory()
    filenameb = re.sub('/', r'\\', filenameb)
    print(filenameb)
    return filenameb
    

def searchFile(self):
    filenamea = findFile1(self)
    filenameb = findFile2(self)
    files = os.listdir(filenamea)
    today = datetime.now()
    def copy_files():
        for i in range(len(files)):
            mod_date = datetime.fromtimestamp(getmtime(('{}\\{}'.format(filenamea, files[i]))))
            mod_date_limit = mod_date + timedelta(days = 1)
            if mod_date_limit > today:
                print('{}\\{}'.format(filenamea, files[i]))
                stl.copy(('{}\\{}'.format(filenamea, files[i])), ('{}'.format(filenameb)))
    copy_files()
    


if __name__ == '__main__':
    pass
