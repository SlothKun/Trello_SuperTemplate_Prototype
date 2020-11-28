import sys
import dboperations

db = dboperations.dboperations()
db.connect()

def getusers():
    return db.GET_users()

def print_user():
    users = db.GET_users()
    nboption = 1
    userselection = {}
    print("""    Users 
    -----""")
    for user in users:
        print("{0} - {1}".format(nboption, user[1]))
        userselection[nboption] = user
        nboption += 1
    return userselection, nboption

def user_selection():
    users = getusers()
    nboption = 1
    userchosen = -1
    userselection = {}
    if len(users) == 1:
        print("User '{0}' chosen !".format(users[0][1]))
        return users[0]
    else:
        print("""    Users 
        -----""")
        for user in users:
            print("{0} - {1}".format(nboption, user[1]))
            userselection[nboption] = user
            nboption += 1

        while userchosen < 0 or userchosen > nboption:
            try:
                userchosen = int(input("Please choose the user (0 to leave) : "))
            except Exception as e:
                userchosen = -1

        if userchosen == 0:
            sys.exit(0)
        else:
            print("User '{0}' chosen !".format(userselection[userchosen][1]))
            return userselection[userchosen]

def user_creation():
    username = ""
    while username == "":
        username = input("Please enter your username : ")

    apikey = input("Please enter your trello APIKEY : ")
    apitoken = input("Please enter your trello APITOKEN : ")
    db.INS_user(username, apikey, apitoken)

def user_deletion():
    alluser, usercount = print_user()
    userchosen = ''
    while userchosen not in [str(i) for i in range(0, usercount+1)]:
        userchosen = input("Please select the user you want to delete (0 to leave) : ")

    if userchosen == 0:
        sys.exit(0)
    else:
        db.DEL_user(alluser[int(userchosen)][1])
