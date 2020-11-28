import sqlite3


class dboperations():
    def __init__(self):
        self.db = ""
        self.user = ""
        self.template = ""
        self.DBPATH = "config/Templates.db"

    def connect(self):
        try:
            self.db = sqlite3.connect(self.DBPATH)
            print("Connected to database !")
        except Exception as e:
            print("An error occured : %d" % e)

    def GET_users(self):
        return self.db.execute('''SELECT * FROM user''').fetchall()

    def GET_template(self):
        return self.db.execute('''SELECT name FROM template''').fetchall()

    def GET_list(self, template):
        return self.db.execute('''SELECT name FROM list join template on templateid = template.id where templateid = %d''' % template).fetchall()

    def GET_cards(self, list):
        return self.db.execute('''SELECT name FROM card join list on listid = list.id where templateid = %d''' % list).fetchall()

    def INS_user(self, username, apikey, apitoken):
        self.db.execute('''INSERT INTO user (username, apikey, apitoken) VALUES (?, ?, ?)''', (username, apikey, apitoken))
        self.db.commit()
        print("User {0} has been successfully added !".format(username))

    def DEL_user(self, username):
        self.db.execute('''DELETE FROM user WHERE username=?''', username)
        self.db.commit()
        print("User {0} has been successfully deleted !".format(username))