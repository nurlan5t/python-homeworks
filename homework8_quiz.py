# Используя классы и все принципы ООП, сделать программу Quiz.
# Которая имеет функции добавить вопрос(Класс Question(title, options)) и пройти тест,
# + записывает результаты в файл и записывает сами вопросы.
# Функционал разделите по файлам, а запуск происходит в main файле.

from utils.classes import Questions
from utils.functions import write_to_file
from utils.functions import read_from_file

class Answers(Questions):
    def __init__(self, title, options, user_option):
        super(Answers, self).__init__(title, options)
        self.user_option = user_option

while 1:
    print('1) Добавить вопрос: ')
    print('2) Пройти тест: ')
    option = int(input('Выбрать вариант: '))
    if option == 1:
        title = input('Введите вопрос: ')
        right_option = input(f'Установите правильный ответ: ')
        write_to_file(f'{title}')
        for i in range(3):
            i = i + 1
            options = input(f'{i}) Введите варианты ответов: ')
            write_to_file(f'{options} ?')

    if option == 2:
        name = input('Введдите ваше имя: ')
        lines = read_from_file()
        for i in lines:
            print(i)
        user_option = input('Введите правильный ответ: ')
        if user_option == right_option:
            res = 'Тест пройден!'
            print(res)
            write_to_file(f'{name.title()} ответ - {user_option} ({res})')
            break
        else:
            res = 'Тест не пройден!'
            write_to_file(f'{name.title()} ответ - {right_option} ({res})')
            print(res)
