import dboperations
import menus
import basicoperations as bo
import sys

users = bo.getusers()

if len(users) != 0:
    menus.mainmenu()

else:
    answerinput = ""
    while answerinput not in ['y', 'n']:
        answerinput = input("No user found ! Create one ? (y/n) : ")
    if answerinput == 'y':
        bo.user_creation()
    else:
        print('Understandable, have a good day')
        sys.exit(0)
