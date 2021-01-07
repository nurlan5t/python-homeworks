''' Написать queue в ООП варианте. В классе должно быть
 состояние хранящее со списком и метод pop()'''
from collections import deque
class My_list():
        q = deque()
        q.append('a')
        q.append('b')
        q.append('c')
        print("Initial queue")
        print(q)
        print("\nElements dequeued from the queue")
        print(q.pop())
        print(q.pop())
        print(q.pop())
        print("\nQueue after removing elements")
        print(q)
My_list()
