import requests


class ApiOp():
    def __init__(self, username, key, token):
        self.username = username
        self.key = key
        self.token = token

    def get_allboards(self):
        response = requests.get('https://api.trello.com/1/member/%s/boards' % self.username, params={'key':self.key, 'token':self.token}).json()
        tables = {}
        for table in response:
            tables[table['name']] = table['id']
        return tables

    def get_alllists(self, boardid):
        response = requests.get('https://api.trello.com/1/board/%s/lists' % boardid, params={'key':self.key, 'token':self.token}).json()
        tables = {}
        for table in response:
            tables[table['name']] = [table['id'], "(included)"]
        return tables

    def get_cards_inlist(self, listid):
        response = requests.get('https://api.trello.com/1/lists/%s/cards' % listid, params={'key':self.key, 'token':self.token}).json()
        tables = {}
        for table in response:
            tables[table['name']] = table['id']
        return tables