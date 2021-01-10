import sqlite3

class dboperations():
    def __init__(self):
        self.db = ""
        self.DBPATH = "config/Templates.db"

    def connect(self):
        try:
            self.db = sqlite3.connect(self.DBPATH)
            print("Connected to the database !\n")
        except Exception as e:
            print("An error occured : %d" % e)

    def get_users(self):
        return self.db.execute('''SELECT * FROM user''').fetchall()

    def get_userid(self, username):
        return self.db.execute('''SELECT id FROM user WHERE username=?''', (username,)).fetchall()[0][0]

    def get_apikey(self, username):
        return self.db.execute('''SELECT apikey FROM user WHERE username=?''', (username,)).fetchall()[0][0]

    def get_apitoken(self, username):
        return self.db.execute('''SELECT apitoken FROM user WHERE username=?''', (username,)).fetchall()[0][0]

    def get_templates(self, boardid):
        return self.db.execute('''SELECT * FROM template WHERE trello_boardid =?''', (boardid,)).fetchall()

    def get_list(self, template):
        return self.db.execute('''SELECT name FROM list join template on templateid = template.id where templateid = %d''' % template).fetchall()

    def get_cards(self, list):
        return self.db.execute('''SELECT name FROM card join list on listid = list.id where templateid = %d''' % list).fetchall()

    def ins_user(self, username, apikey, apitoken):
        self.db.execute('''INSERT INTO user (username, apikey, apitoken) VALUES (?, ?, ?)''', (username, apikey, apitoken))
        self.db.commit()
        print("User '{0}' has been successfully added !".format(username))

    def ins_template(self, template_name, boardid, username):
        self.db.execute('''INSERT INTO template (name, trello_boardid, userid) VALUES (?, ?, ?)''', (template_name, boardid, self.get_userid(username)))
        self.db.commit()
        print("Template '{0}' has been successfully added !".format(template_name))

    def del_user(self, username):
        self.db.execute('''DELETE FROM user WHERE username=?''', (username,))
        self.db.commit()
        print("User '{0}' has been successfully deleted !".format(username))

    def del_template(self, templatename):
        self.db.execute('''DELETE FROM template WHERE name=?''', (templatename,))
        self.db.commit()
        print("Template '{0}' has been successfully deleted !".format(templatename))