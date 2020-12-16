#Задание 3.
# Создать классы Cat, Dog которые будут наследоватся от класса Animal.

class Animal:
    def can_eat(self):
        print('i can Eat')

    def can_move(self):
        print('i can Move')

class Dog(Animal):
    def make_noize(self):
       print('Bark!, Bark!')

class Cat(Animal):
    def make_noize(self):
        print('Meowww...')

Nemo = Animal()
Nemo.can_eat()
Nemo.can_move()

Rex = Dog()
Rex.can_move()
Rex.make_noize()

Tom = Cat()
Tom.can_eat()
Tom.make_noize()
