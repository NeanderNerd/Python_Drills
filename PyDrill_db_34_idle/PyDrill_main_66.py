##  Python: 3.6.0
##
##  Author: Christopher Garrick
##
##  Purpose:  The Tech Academy - Python Course, Item 66
##            PyDrill_db_34_idle
##            Create a database for a program that will transfer files updated
##            within the last 24 hours that stores the all previous days and
##            times the program was ran.


from tkinter import *
import tkinter as tk
import PyDrill_gui_66
import PyDrill_func_66


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(215, 325)
        self.master.maxsize(215, 325)
        PyDrill_func_66.center_window(self, 215, 325)
        self.master.title('File Transfer')
        self.master.configure(bg = '#00AABD')
        self.master.protocol('WM_DELETE_WINDOW', lambda: PyDrill_func_66.ask_quit(self))

        PyDrill_gui_66.load_gui(self)
        PyDrill_func_66.create_db(self)
        PyDrill_func_66.pop_lst(self)


if __name__ == '__main__' :
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
