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
import PyDrill_gui
import PyDrill_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(100, 100)
        self.master.maxsize(100, 100)
        PyDrill_func.center_window(self, 100, 100)
        self.master.title('File Transfer')
        self.master.configure(bg = '#00AABD')
        self.master.protocol('WM_DELETE_WINDOW', lambda: PyDrill_func.ask_quit(self))

        PyDrill_gui.load_gui(self)


if __name__ == '__main__' :
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
