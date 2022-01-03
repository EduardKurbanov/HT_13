"""
2. Створити клас Person, в якому буде присутнім метод __init__ який буде приймати * аргументів,
    які зберігатиме в відповідні змінні. Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
   - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession.
"""


class Peson(object):
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def show_age(self):
        return self.__age

    def print_name(self):
        print(f"name: {self.__name}")

    def show_all_information(self):
        print(f"name: {self.__name}\n"
              f"age: {self.__age}")


p_1 = Peson("Anton", 25)
print(p_1.show_age())
p_1.print_name()
p_1.show_all_information()
p_1.profession = "IT"

p_2 = Peson("Tom", 30)
print(p_1.show_age())
p_2.print_name()
p_2.show_all_information()
p_2.profession = "HR"

print(p_1.__dict__)
print(p_2.__dict__)
