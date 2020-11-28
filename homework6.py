class Account:
    def __init__(self, login, password):
        self._login = login
        self._password = password

    @property
    def login(self):
        return self._login
    @login.setter
    def login(self, value):
        print(value)
        print("Special Login can't be changed")

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, value):
        print(value)
        print("Special password can't be changed")

    def __str__(self):
        return f"{self.login} \n {self.password}"

while True:
    print('1) Create user: ')
    print('2) Change login and password: ')
    print('3) Show login and password: ')
    option = int(input('Choose option'))
    if option == 1:
        inp_login = input('Enter your login')
        inp_password = input('Enter your password')
        a = Account(inp_login, inp_password)
    if option == 2:
        a.login = input('Enter new login')
        a.password = input('Enter new password')
    if option == 3:
        print(a)