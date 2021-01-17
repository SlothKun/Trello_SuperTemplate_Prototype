import sys

class menus():
    def __init__(self, bo):
        self.bo = bo

    def usermenu(self):
        print("""1 - Select user
2 - Create user
3 - Delete user
4 - Exit\n""")
        option = 0
        while option not in ['1', '2', '3', '4']:
            option = input("Select an option : ")

        if option == '1':
            self.bo.user_selection()
        elif option == '2':
            self.bo.user_creation()
        elif option == '3':
            self.bo.user_deletion()
        else:
            sys.exit(0)

    def tablemenu(self):
        print("""1 - Select board
2 - Go back
3 - Exit\n""")
        option = 0
        while option not in ['1', '2', '3']:
            option = input("Select an option : ")

        if option == '1':
            self.bo.board_selection()
        elif option == '2':
            self.usermenu()
        else:
            sys.exit(0)

    def templatemenu(self):
        print("""1 - Select template
2 - Create template
3 - Delete template
4 - Go back
5 - Exit\n""")
        option = 0
        while option not in ['1', '2', '3', '4', '5']:
            option = input("Select an option : ")

        if option == '1':
            self.bo.template_selection()
            # Todo - Call template selection
        elif option == '2':
            self.bo.template_creation()
            # Todo - Call template creation
        elif option == '3':
            self.bo.template_deletion()
            # Todo - Call template deletion
        elif option == '4':
            self.tablemenu()
        else:
            sys.exit(0)
