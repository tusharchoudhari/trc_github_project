def print_users(user,*users):
    print('First user argument:{}'.format(user))
    for user in users:
        print('user received from variable length  argument:{}'.format(user))

print_users('edureka','admin','ceo','manage','worker')