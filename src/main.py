import dboperations
import basicoperations as bo
import sys

users = bo.getusers()
print(users)


if len(users) != 0:
    print("""1 - Select user
2 - Create user
3 - Delete user
4 - Exit\n""")

    option = 0
    while option not in ['1', '2', '3', '4']:
        option = input("Select an option : ")

    if option == '1':
        a = bo.user_selection()
    elif option == '2':
        bo.user_creation()
    elif option == '3':
        bo.user_deletion()
    else:
        sys.exit(0)




else:
    answerinput = ""
    while answerinput not in ['y', 'n']:
        answerinput = input("No user found ! Create one ? (y/n) : ")
    if answerinput == 'y':
        bo.user_creation()
    else:
        print('Understandable, have a good day')
        sys.exit(0)
