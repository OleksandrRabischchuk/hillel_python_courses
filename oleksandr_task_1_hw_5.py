user_password = input('insert your password: ')
user_copy = user_password
user_password_repeat = input('insert your password repeat: ')
while True:
    if user_password_repeat == user_copy:
        print('Welcome')
        break
    else:
        user_password_repeat = input('password its wrong,repeat please: ')
        continue
