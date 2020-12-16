name = input('Введите ваше имя: ')
month = input('Введите месяц начала обучения: ')

if month == 'ноябрь':
    print(name.title() + ', Вы на первом месяце обучения.')

elif month == 'декабрь':
    print(name.title() + ', Вы на втором месяце обучения.')

elif month == 'январь':
    print(name.title() + ', Вы на третьем месяце обучения.')

elif month == 'февраль':
    print(name.title() + ', Вы на четвертом месяце обучения.')

else:
    print('Данные введены неправильно!')