# Игру камень - ножница - бумага написать с помощью ООП.
# - Пользователь выбирает одну из камень - ножница - бумага.
# - Компьютер делает выбор рандомно
# - Результат показывает выиграл ли пользователь.
# - Создайте такие классы как Game, User.
# - Опишите состояние и методы данных классов.
import random

class Game:
    def __init__(self, user_win=0, comp_win=0):
        self.user_win = user_win
        self.comp_win = comp_win

    def play(self):
        global user
        attempts = int(input('How many attempts? '))
        count = 0
        user_win = 0
        comp_win = 0
        while attempts > 0:
            attempts = attempts - 1
            count += 1
            comp = random.randint(1,3)
            user = User()
            user = user.user_choose()
            if user == comp:
                print('Draw!')
            elif user==1 and comp==2 or user==2 and comp==3 or user==3 and comp==1:
                print('You win!')
                user_win += 1
            elif user==1 and comp==3 or user==2 and comp==1 or user==3 and comp==2:
                print('You lose!')
                comp_win += 1
            else:
                print('Error, try again!')
                count -= 1
            draws = count - (user_win + comp_win)

            print(f'Games: {count} \n User: {user_win} \n Comp: {comp_win} \n Draws: {draws} \n Attempts Possible: {attempts}')

class User:
    def user_choose(self):
        user = int(input('Choose the option: |1) Stone  |2) Scissors  |3) Paper : '))
        return user

game = Game()
game.play()