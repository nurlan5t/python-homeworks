'''Написать Fibonacci sequence с помощью рекурсивного метода.
Пользователь вводит число(например 8) и программа
должна вывести числа Фибоначчи до 8.'''

num = int(input('Enter integer number: '))
print(f'Fibonacci sequence of: {num}')
n1, n2 = 0, 1
count = 0
if num <= 0:
    print('Enter a positive number!')
elif num == 1:
    print('It is not serious number :D ')
else:
    while count < num:
        print(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        count += 1
