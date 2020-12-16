print('Это Список ежедневных задач, пиши сюда чтобы не забыть!')
tasks = []
while True:
    print('1) Добавить задачу')
    print('2) Показать все задачи')
    print('3) Завершить задачу')
    option = int(input('Выберите вариант: '))

    if option == 1:
        task = input('Введите что нужно сделать сегодня. ')
        tasks.append(task)

    if option == 2:
        for i in tasks:
            print(f'{i}')

    if option == 3:
        idx = int(input('Введите индекс '))
        tasks.insert(idx, f'задача под индексом {idx} сделана')
        idx = idx + 1
        del tasks[idx]

#Доп: Сделать программу to do list, которая записывает ваши задачи
#и их по индексам можно отмечать как сделанные