import sys
import dboperations
import restapioperations as apiop

#db = dboperations.dboperations()
#db.connect()

class baseoperations():
    def __init__(self):
        self.username = ""
        self.key = ""
        self.token = ""
        self.board = ""
        self.template = ""
        self.db = dboperations.dboperations()

    def dbconnect(self):
        self.db.connect()

    def getusers(self):
        return self.db.GET_users()

    def getboards(self):
        self.key = self.db.GET_apikey(self.username)
        self.token = self.db.GET_apitoken(self.username)
        return apiop.GET_allboards(self.username, self.key, self.token)

    def user_printing(self):
        users = self.getusers()
        nboption = 1
        userselection = {}
        if len(users) == 1:
            userselection[str(nboption)] = users[0]
        else:
            print("""    Users 
            -----""")
            for user in users:
                print("{0} - {1}".format(nboption, user[1]))
                userselection[str(nboption)] = user
                nboption += 1
        return userselection, nboption

    def user_selection(self):
        alluser, usercount = self.user_printing()
        userchosen = ''

        if usercount == 1:
            userchosen = '1'
        else:
            while userchosen not in [str(i) for i in range(0, usercount+1)]:
                userchosen = input("Please choose the user (0 to leave) : ")

        if userchosen == '0':
            sys.exit(0)
        else:
            self.username = alluser[userchosen][1]
            print("\nUser '{0}' chosen !\n".format(alluser[userchosen][1]))

    def user_creation(self):
        username = ""
        while username == "":
            username = input("Please enter your trello username (@username) : ")

        if username[0] == "@":
            username = username[1:]
        apikey = input("Please enter your trello APIKEY : ")
        apitoken = input("Please enter your trello APITOKEN : ")
        self.db.INS_user(username, apikey, apitoken)

    def user_deletion(self):
        alluser, usercount = self.user_printing()
        userchosen = ''
        while userchosen not in [str(i) for i in range(0, usercount+1)]:
            userchosen = input("Please select the user you want to delete (0 to leave) : ")

        if userchosen == 0:
            sys.exit(0)
        else:
            self.db.DEL_user(alluser[int(userchosen)][1])

    def board_printing(self):
        boards = self.getboards()
        nboption = 1
        boardselection = {}
        print("""    Boards 
    ------""")
        for name, id in boards.items():
            print("{0} - {1}".format(nboption, name))
            boardselection[str(nboption)] = (name, id)
            nboption += 1
        return boardselection, nboption

    def board_selection(self):
        allboard, boardscount = self.board_printing()
        boardchosen = ''
        #print(allboard)
        while boardchosen not in [str(i) for i in range(0, boardscount+1)]:
            boardchosen = input("Please choose the board (0 to leave) : ")

        if boardchosen == '0':
            sys.exit(0)
        else:
            self.board = allboard[boardchosen]
            print("Board '{0}' chosen !".format(allboard[boardchosen][0]))