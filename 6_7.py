"""
6. Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.
7. Створити пустий клас, який називається Thing. Потім створіть об'єкт example цього класу. Виведіть типи зазначених об'єктів.
"""
# 6. ******************************************************************

class Count(object):
    __conut: int = 0

    def get_count(self):
        Count.__conut += 1
        print(f"conut -> {Count.__conut}")


a_1 = Count()
a_1.get_count()
a_2 = Count()
a_2.get_count()


# 7. ******************************************************************

class Thing(object):
    pass


example = Thing()

print(f"type -> {type(example)}")
