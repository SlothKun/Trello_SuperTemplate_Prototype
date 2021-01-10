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
        self.api = ""


    def dbconnect(self):
        self.db.connect()


    def getusers(self):
        return self.db.get_users()


    def getboards(self):
        self.key = self.db.get_apikey(self.username)
        self.token = self.db.get_apitoken(self.username)
        # to-do : Create self api elsewhere
        self.api = apiop.ApiOp(self.username, self.key, self.token)
        return self.api.get_allboards()


    def gettemplates(self):
        return self.db.get_templates(self.board[1])


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
        self.db.ins_user(username, apikey, apitoken)


    def user_deletion(self):
        allusers, usercount = self.user_printing()
        userchosen = ''
        while userchosen not in [str(i) for i in range(0, usercount+1)]:
            userchosen = input("Please select the user you want to delete (0 to leave) : ")

        if userchosen == 0:
            sys.exit(0)
        else:
            self.db.del_user(allusers[int(userchosen)][1])


    def boards_printing(self):
        boards = self.getboards()
        nboption = 1
        boardselection = {}

        if len(boards) == 1:
            # to-do : test this one
            boardselection[str(nboption)] = (boards.keys()[0], id.values()[0])
        else:
            print("""    Boards 
    ------""")
            for name, id in boards.items():
                print("{0} - {1}".format(nboption, name))
                boardselection[str(nboption)] = (name, id)
                nboption += 1
        return boardselection, nboption


    def lists_printing(self, lists):
        nboption = 1
        listselection = {}
        print("""    Lists 
    -----""")
        for name, id in lists.items():
            print("{0} - {1} {2}".format(nboption, name, id[1]))
            listselection[str(nboption)] = (name, id)
            nboption += 1
        return listselection, nboption


    def templates_printing(self):
        templates = self.gettemplates()
        #print(templates)
        nboption = 1
        templateselection = {}
        print("""    Templates 
            --------""")
        for template in templates:
            print("{0} - {1}".format(nboption, template[1]))
            templateselection[str(nboption)] = template
            nboption += 1
        return templateselection, nboption


    def board_selection(self):
        allboards, boardscount = self.boards_printing()
        boardchosen = ''
        #print(allboard)
        if (boardscount == 1):
            boardchosen = '1'
        else:
            while boardchosen not in [str(i) for i in range(0, boardscount+1)]:
                boardchosen = input("Please choose the board (0 to leave) : ")

        if boardchosen == '0':
            sys.exit(0)
        else:
            self.board = allboards[boardchosen]
            print("Board '{0}' chosen !".format(allboards[boardchosen][0]))
            #self.gettemplates()


    def template_creation(self):
        lists = self.api.get_alllists(self.board[1])
        user_input = ''
        activation_control = {"(included)":"(excluded)", "(excluded)":"(included)"}

        while True:
            options, nboption = self.lists_printing(lists)
            user_input = input("Select the list to exclude/include in the template (0 to continue) : ")
            if user_input == '0':
                break
            else:
                options[user_input][1][1] = activation_control[options[user_input][1][1]]
                # to-do: The solution below is stupid, i'll have to change it later
                lists = {}
                for option in options.items():
                    lists[option[1][0]] = option[1][1]

        # to-do: add confirmation (put name choice in a function and call it)
        template_name = ""
        while template_name == "":
            template_name = input("Please enter the template name : ")

        # to-do : add lists, card ... entries in db
        self.db.ins_template(template_name, self.board[1], self.username)


    def template_selection(self):
        alltemplates, templatescount = self.templates_printing()
        templatechosen = ''
        #print(alltemplates)
        if templatescount == 1:
            templatechosen = '1'
        else:
            while templatechosen not in [str(i) for i in range(0, templatescount+1)]:
                templatechosen = input("Please choose the board (0 to leave) : ")

        if templatechosen == '0':
            sys.exit(0)
        else:
            self.template = alltemplates[templatechosen]
            print("Template '{0}' chosen !".format(alltemplates[templatechosen][1]))
            print("Applying now...")
            # to-do : apply template

    def template_deletion(self):
        alltemplates, templatecount = self.templates_printing()
        templatechosen = ''
        while templatechosen not in [str(i) for i in range(0, templatecount+1)]:
            templatechosen = input("Please select the user you want to delete (0 to leave) : ")

        if templatechosen == 0:
            sys.exit(0)
        else:
            self.db.del_template(alltemplates[templatechosen][1])