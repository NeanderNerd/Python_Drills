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
import PyDrill_main_66
import PyDrill_func_66


def load_gui(self):

    self.lbl_list = tk.Label(self.master, text = 'Last run time:', bg = '#00AABD', fg = '#FFFFFF')
    self.lbl_list.grid(row = 0, column = 0, padx = 5)
    self.lbl_src = tk.Label(self.master, text = 'Source: ', bg = '#00AABD', fg = '#FFFFFF')
    self.lbl_src.grid(row = 5, column = 0, padx = 5, pady = 5, sticky = 'w')
    self.lbl_dest = tk.Label(self.master, text = 'Destination: ', bg = '#00AABD', fg = '#FFFFFF')
    self.lbl_dest.grid(row = 5, column = 0, padx = 5, pady = 5, sticky = 'e')
    self.txt_src = tk.Entry(self.master, text = '', width = 15)
    self.txt_src.grid(row = 6, column = 0, padx = 5, pady = 5, sticky = 'w')
    self.txt_dest = tk.Entry(self.master, text = '', width = 15)
    self.txt_dest.grid(row = 6, column = 0, padx = 5, pady = 5, sticky = 'e')
    self.btn_src = tk.Button(self.master, width = 5, height = 1, text = 'Source', command = lambda: PyDrill_func_66.findFile1(self))
    self.btn_src.grid(row = 7, column = 0, padx = 5, pady = 5, sticky = 'w')
    self.btn_dest = tk.Button(self.master, width = 8, height = 1, text = 'Destination', command = lambda: PyDrill_func_66.findFile2(self))
    self.btn_dest.grid(row = 7, column = 0, padx = 5, pady = 5, sticky = 'e')
    self.btn_search = tk.Button(self.master, width = 4, height = 1, text = 'Search', command = lambda: PyDrill_func_66.searchFile(self))
    self.btn_search.grid(row = 8, column = 0, padx = 5, pady = 5, sticky = 'nsew' )
    self.scrollbar1 = Scrollbar(self.master, orient = VERTICAL)
    self.lstList1 = Text(self.master, yscrollcommand = self.scrollbar1.set, height = 10, width = 25)
    self.scrollbar1.config(command = self.lstList1.yview)
    self.lstList1.grid(row = 1, column = 0, rowspan = 4, padx = 5, pady = 5, sticky = 'nsew')
    self.lstList1.config(wrap = WORD)

filenamea = ''
filenameb = ''


if __name__ == '__main__':
    pass
