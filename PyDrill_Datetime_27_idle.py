##  Python:  2.7.13
##
##  Author:  Christopher Garrick
##
##  Purpose:  The Tech Academy - Python Course, Item 62
##            Python Drill_Daytime_27_idle
##            A program to determin if New York and London branches
##            are open from the time in Portland.


import datetime
from datetime import datetime


moment = int(datetime.now().hour)

def Branches(moment):
    if (moment + 3) < 9 or (moment + 3) >= 21:
        print('New York Branch Closed')
    elif (moment + 3) > 9 or (moment + 3) < 21:
        print('New York Branch Open')
    if (moment + 8) < 9 or (moment + 8) >= 21:
        print('London Branch Closed')
    elif (moment + 8) > 9 or (moment + 8) < 21:
        print('London Branch Open')

Branches(moment)
