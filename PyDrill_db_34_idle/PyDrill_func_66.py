##  Python: 3.6.0
##
##  Author: Christopher Garrick
##
##  Purpose:  The Tech Academy - Python Course, Item 66
##            PyDrill_db_34_idle
##            Create a database for a program that will transfer files updated
##            within the last 24 hours that stores the all previous days and
##            times the program was ran.


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
import PyDrill_main_66
import PyDrill_gui_66
from PyDrill_gui_66 import *
import sqlite3




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

def create_db(self):
    conn = sqlite3.connect('run.db')
    with conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS tbl_checkIn( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                    col_date TEXT,\
                    col_time TEXT \
                    );')
        conn.commit()
    conn.close()

def pop_lst(self):
    conn = sqlite3.connect('run.db')
    with conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM tbl_checkIn')
        var_full = cur.fetchall()
        self.lstList1.insert(END, var_full)
    conn.close()

def findFile1(self):
    global filenamea
    filenamea = askdirectory()
    filenamea = re.sub('/', r'\\', filenamea)
    print(filenamea)
    return filenamea


def findFile2(self):
    global filenameb
    filenameb = askdirectory()
    filenameb = re.sub('/', r'\\', filenameb)
    print(filenameb)
    return filenameb
    

def searchFile(self):
    files = os.listdir(filenamea)
    today = datetime.now()
    var_date = datetime.today().strftime("%m/%d/%Y")
    var_time = datetime.now().strftime('%H:%M:%S')
    conn = sqlite3.connect('run.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO tbl_checkIn (col_date, col_time) VALUES ('{}', '{}')""".format(var_date, var_time))
        cursor.execute('''SELECT COUNT(ID) FROM tbl_checkIn''')
        num = cursor.fetchone()[0]
        cursor.execute('''SELECT * FROM tbl_checkIn WHERE ID LIKE {}'''.format(num))
        var_full = cursor.fetchall()
        self.lstList1.insert(END, var_full)
        conn.commit()
    conn.close()
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
