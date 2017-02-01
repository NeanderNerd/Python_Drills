##  Python: 3.6.0
##
##  Author: Christopher Garrick
##
##  Purpose:  The Tech Academy - Python Course, Item 65
##            PyDrill_gui_34_idle
##            Create a GUI for a program that will transfer files updated
##            within the last 24 hours.

from tkinter import *
import tkinter as tk
import PyDrill_main
import PyDrill_func


def load_gui(self):


    self.btn_search = tk.Button(self.master, width = 6, height = 1, text = 'Search', command = lambda: PyDrill_func.searchFile(self))
    self.btn_search.place(x = 34, y = 35)


if __name__ == '__main__':
    pass
