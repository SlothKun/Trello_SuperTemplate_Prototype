import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

class ApiOp():
    def __init__(self, username, key, token):
        self.username = username
        self.key = key
        self.token = token

    def get_allboards(self):
        response = requests.get('https://api.trello.com/1/member/%s/boards' % self.username,
                                params={'key': self.key,
                                        'token': self.token}).json()
        tables = {}
        for table in response:
            tables[table['name']] = table['id']
        return tables

    def get_alllists(self, boardid):
        response = requests.get('https://api.trello.com/1/board/%s/lists' % boardid,
                                params={'key': self.key,
                                        'token': self.token}).json()
        alllists_data = {}
        print("all lists response : ")
        pp.pprint(response)
        pos = 0
        for listdata in response:
            alllists_data[listdata['name']] = [listdata['id'], "(included)", pos]
            pos += 1
        return alllists_data

    def get_cards_inlist(self, listid):
        """
            Call Trello's REST API for all cards in specified list\n
            Only retrieve name, id, desc & card'labels
        """
        response = requests.get('https://api.trello.com/1/lists/%s/cards' % listid,
                                params={'key': self.key,
                                        'token': self.token}).json()
        allcards = {}
        print("card in list : ")
        #pp.pprint(response)
        pos = 0
        for card in response:
            allcards[card['name']] = [card['id'], card['desc'],
                                      card['labels'], pos]
            pos += 1
        pp.pprint(allcards)
        return allcards

    def get_alllabels(self, boardid):
        """
            Call Trello's REST API for all labels in specified board
        """
        response = requests.get('https://api.trello.com/1/boards/%s/labels' % boardid,
                                params={'key': self.key,
                                        'token': self.token}).json()
        print("\nall_labels : ")
        pp.pprint(response)
        return response
