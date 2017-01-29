##  Python:  2.7.13
##
##  Author: Christopher Garrick
##
##  Purpose:  The Tech Academy - Python Course, Item 63
##            PyDrill_shutil_module_27_idle
##            A program to move files from one folder to another.


import shutil as stl
import os

def move_files():
    files = os.listdir('C:\\Users\\Student\\Desktop\\Folder A')
    while files:
        print("C:\Users\Student\Desktop\Folder A\ " + files[0])
        stl.move('C:\\Users\\Student\\Desktop\\Folder A\\{}'.format(files[0]), 'C:\\Users\\Student\\Desktop\\Folder B')
        files = os.listdir('C:\\Users\\Student\\Desktop\\Folder A')

move_files()
