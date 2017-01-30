##  Python:  2.7.13
##
##  Author: Christopher Garrick
##
##  Purpose:  The Tech Academy - Python Course, Item 64
##            PyDrill_scripting_27_idle
##            A program to copy files from one folder to another
##            if it has been modified in the last 24 hrs.


import shutil as stl
import os
import datetime
from datetime import datetime
from os.path import getmtime
from datetime import timedelta

files = os.listdir('C:\\Users\\Student\\Desktop\\Folder A')
today = datetime.today()

def copy_files():
    for i in range(int(len(files))):
        mod_date = datetime.fromtimestamp(getmtime('C:\\Users\\Student\\Desktop\\Folder A\\{}'.format(files[i])))
        mod_date_limit = mod_date + timedelta(days = 1)
        if mod_date_limit > today:
            print("C:\Users\Student\Desktop\Folder A\ " + files[i])
            stl.copy('C:\\Users\\Student\\Desktop\\Folder A\\{}'.format(files[i]), 'C:\\Users\\Student\\Desktop\\Folder B')

copy_files()
