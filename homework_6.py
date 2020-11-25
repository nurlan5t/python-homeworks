class Account:
    def __init__(self, login, password):
        self.login = login
        self._password = password

    # @property
    # def login(self):
    #     return self.login
    # @login.setter
    # def login(self, value):
    #     print(value)
    #     print("Special Login can't be changed")

user1 = Account('JamesBond', '007')
# user1.login = 'qwe'

check = input(f'Hi, {user1.login}! \nPlease, enter yor password: ')
if check == '007':
    print('Access is open!')
else:
    print(f'Password not correct, you are not {user1.login}!')