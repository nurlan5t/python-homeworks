# Задание 2. Создать 3 класса (Rectangle, Circle, Square) с методом get_area(),
# который возвращает площадь объекта.

class Square:
    sides = 5
    def get_area(self):
        print(self.sides**2)

class Rectangle:
    length = 5
    width = 2
    def get_area(self):
       print(self.length * self.width)

class Circle:
    radius = 5
    def get_area(self):
        print(self.radius**2 * 3.14)

b = Square()
b.get_area()

a = Rectangle()
a.get_area()

c = Circle()
c.get_area()