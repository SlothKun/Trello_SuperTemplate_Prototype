import sqlite3

class dboperations():
    def __init__(self):
        self.db = ""
        self.user = ""
        self.template = ""

    def connect(self):
        try:
            self.db = sqlite3.connect("config/Templates.db")
            print("Connected to database !")
        except Exception as e:
            print("An error occured : %d" % e)

    def GET_users(self):
        return self.db.execute('''SELECT username FROM user''')

    def GET_template(self):
        return self.db.execute('''SELECT name FROM template''')

    def GET_list(self, template):
        return self.db.execute('''SELECT name FROM list join template on templateid = template.id where templateid = %d''' % template)

    def GET_cards(self, list):
        return self.db.execute('''SELECT name FROM card join list on listid = list.id where templateid = %d''' % list)
