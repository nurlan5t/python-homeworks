# Задание 1. Создать класс UserProfile с атрибутами
# name, phone_number, password и инкапсулируйте их.

class UserProfile:
    __name = 'Alex'
    __phone_number = 123456789
    __password = 123456

    def get_data(self):
        return self.__name

a = UserProfile()
print(a.get_data())