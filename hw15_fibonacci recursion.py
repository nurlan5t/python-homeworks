'''Написать Fibonacci sequence с помощью рекурсивного метода.
Пользователь вводит число(например 8) и программа
должна вывести числа Фибоначчи до 8.'''

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input('Enter integer number: '))

if nterms <= 0:
   print("Please enter a positive integer: ")
else:
   print(f"Fibonacci sequence: {nterms}")
   for i in range(nterms):
       print(recur_fibo(i))
