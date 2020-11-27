class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        new_numerator = self.numerator + other.numerator
        new_denominator = self.denominator + other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator - other.numerator
        new_denominator = self.denominator - other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator / other.numerator
        new_denominator = self.denominator / other.denominator
        return Fraction(new_numerator, new_denominator)

    def __str__(self):
        return f"{self.numerator}\n{max(len(str(self.denominator)), len(str(self.numerator))) * '-'}\n{self.denominator}"

first_numerator = int(input('1) Enter numerator:   '))
first_denominator = int(input('1) Enter denominator: '))
fraction1 = Fraction(first_numerator, first_denominator)

chosen_operator = input('|+|  |-|  |*|  |/| ')

second_numerator = int(input('1) Enter numerator:   '))
second_denominator = int(input('1) Enter denominator: '))
fraction2 = Fraction(second_numerator, second_denominator)

if chosen_operator == '+':
    print(fraction1 + fraction2)

if chosen_operator == '-':
    print(fraction1 - fraction2)

if chosen_operator == '*':
    print(fraction1 * fraction2)

if chosen_operator == '/':
    print(fraction1 / fraction2)
