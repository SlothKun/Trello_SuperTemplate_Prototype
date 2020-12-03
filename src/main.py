import dboperations
import menus
import basicoperations
import sys

bo = basicoperations.baseoperations()
bo.dbconnect()

users = bo.getusers()
menusobj = menus.menus(bo)

if len(users) != 0:
    menusobj.usermenu()
    menusobj.tablemenu()
else:
    answerinput = ""
    while answerinput not in ['y', 'n']:
        answerinput = input("No user found ! Create one ? (y/n) : ")
    if answerinput == 'y':
        bo.user_creation()
    else:
        print('Understandable, have a good day')
        sys.exit(0)