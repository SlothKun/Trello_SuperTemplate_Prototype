import dboperations
import sys

db = dboperations.dboperations()
db.connect()

users = db.GET_users()


if len(users.fetchall()) == 0:
    optionindex = 1

    print("%i - Select user")
    print("%i - Create user")
    print("%i - Exit")

    print("""Users 
    -----""")
    for user in users:
        print("%i - %d" % optionindex, user)
        optionindex += 1

else:
    answerinput = ""
    while answerinput not in ['y', 'n']:
        answerinput = input("No user found ! Create one ? (y/n) : ")

    if answerinput == 'n':
        print('Understandable, have a good day')
        sys.exit(0)