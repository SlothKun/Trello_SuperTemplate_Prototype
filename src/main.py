import dboperations
import menus
import basicoperations
import sys

'''
    TO-DOs :
        - Add line return (to make it visually better)
'''

print("TEST")


def notfound_continue(object):
    answerinput = ""
    while answerinput not in ['y', 'n']:
        answerinput = input(f"No {object} found ! Create one ? (y/n) : ")
    if answerinput == 'n':
        print("Exiting now..")
        sys.exit(0)


bo = basicoperations.baseoperations()
bo.dbconnect()

users = bo.getusers()
menusobj = menus.menus(bo)

if len(users) != 0:
    menusobj.usermenu()
    menusobj.tablemenu()
    if len(bo.gettemplates()) != 0:
        menusobj.templatemenu()
    else:
        notfound_continue("template")
        bo.template_creation()
else:
    notfound_continue("user")
    bo.user_creation()
