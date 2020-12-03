import requests

def GET_allboards(username, key, token):
    response = requests.get('https://api.trello.com/1/member/%s/boards' % username, params={'key':key, 'token':token}).json()
    tables = {}
    for table in response:
        tables[table['name']] = table['id']
    return tables