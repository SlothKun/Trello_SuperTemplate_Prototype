import sqlite3
import pprint

pp = pprint.PrettyPrinter(indent=4)

class dboperations():
    def __init__(self):
        self.db = ""
        self.DBPATH = "config/Templates.db"

    def connect(self):
        try:
            self.db = sqlite3.connect(self.DBPATH)
            self.db.execute("""PRAGMA foreign_keys = 1;""")
            self.db.commit()
            print(self.db.execute("""PRAGMA foreign_keys;"""))
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
        return self.db.execute('''SELECT * FROM template WHERE trello_boardid=?''', (boardid,)).fetchall()

    def get_templateid(self, templatename, boardid):
        return self.db.execute("""SELECT id FROM template WHERE name=? AND trello_boardid=?""", (templatename, boardid,)).fetchall()[0][0]

    def get_list(self, template):
        return self.db.execute('''SELECT name FROM list join template on templateid = template.id where templateid = %d''' % template).fetchall()

    def get_listid(self, listtrelloid, template_id):
        return self.db.execute("""SELECT id FROM list WHERE trelloid=? AND templateid=?""", (listtrelloid, template_id,)).fetchall()[0][0]

    # Not good
    def get_cards(self, list):
        return self.db.execute('''SELECT name FROM card join list on listid = list.id where templateid = %d''' % list).fetchall()

    def get_cardid(self, listid, cardtrelloid):
        return self.db.execute("""SELECT id FROM card WHERE listid=? AND trelloid=?""", (listid, cardtrelloid)).fetchall()[0][0]

    def get_labelid(self, cardlabeltrelloid):
        return self.db.execute("""SELECT id FROM label WHERE trelloid=?""", (cardlabeltrelloid,)).fetchall()[0][0]

    def ins_user(self, username, apikey, apitoken):
        self.db.execute('''INSERT INTO user (username, apikey, apitoken) VALUES (?, ?, ?)''', (username, apikey, apitoken))
        self.db.commit()
        print("User '{0}' has been successfully added !".format(username))

    def ins_template(self, template_name, boardid, username):
        self.db.execute('''INSERT INTO template (name, trello_boardid, userid)
                            VALUES (?, ?, ?)''',
                        (template_name, boardid, self.get_userid(username)))
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

    def ins_boardlabel(self, template_id, labeltrelloid, labelname, labelcolor):
        self.db.execute("""INSERT INTO label (templateid, trelloid, name, color)
                           VALUES (?, ?, ?, ?)""",
                        (template_id, labeltrelloid, labelname, labelcolor))
        self.db.commit()
        print("Board label '{0}' ({1}) has been successfully added !".format(labelname, labelcolor))

    def ins_list(self, template_id, listtrelloid, listname, listpos):
        self.db.execute("""INSERT INTO list (templateid, trelloid, name, pos)
                            VALUES (?, ?, ?, ?)""",
                        (template_id, listtrelloid, listname, listpos))
        self.db.commit()
        print("List '{0}' has been successfully added !".format(listname))

    def ins_card(self, template_id, list_id, cardtrelloid, cardname, carddesc, cardpos):
        #template_id = self.get_templateid(templatename)
        #list_id = self.get_listid(listname, template_id)
        self.db.execute("""INSERT INTO card (templateid, listid, trelloid, name, pos, desc)
                           VALUES (?, ?, ?, ?, ?, ?)""",
                        (template_id, list_id, cardtrelloid, cardname, cardpos, carddesc))
        self.db.commit()
        print("Card '{0}' has been successfully added !".format(cardname))

    def ins_cardlabel(self, card_id, label_id):
        #cardlabel_id = self.get_labelid(cardlabelname)
        #card_id = self.get_cardid(card_trelloid)
        print(f"cardlabelid {label_id}")
        print(f"cardid {card_id}")
        self.db.execute("""INSERT INTO cardlabel (cardid, labelid)
                           VALUES (?, ?)""",
                        (card_id, label_id))
        self.db.commit()
        #print("Cardlabel '{0}' has been successfully added !".format(cardlabelname))
