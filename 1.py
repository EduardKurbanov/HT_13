"""
1. Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати математичні операції з 2-ма числами, а саме додавання, віднімання, множення, ділення.
   - Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення
   - Якщо використати один з методів - last_result повенен повернути результат виконання попереднього методу.
   - Додати документування в клас (можете почитати цю статтю: https://realpython.com/documenting-python-code/ )
"""


class Calc(object):
    """
    Class attribute << last result >> returns method evaluation
    addition_operation(x: float, y: float)
    subtraction_operatio(x: float, y: float)
    multiplication_operation(x: float, y: float)
    division_operation(x: float, y: float)
    """
    last_result = None

    def addition_operation(self, x: float, y: float):
        """
        :param x: float:
        :param y: float:
        :return: Calc.last_result = x + y
        """
        self.last_result = x + y
        return self.last_result

    def subtraction_operation(self, x: float, y: float):
        """
        :param x: float:
        :param y: float:
        :return: Calc.last_result = x - y
        """
        self.last_result = x - y
        return self.last_result

    def multiplication_operation(self, x: float, y: float):
        """
        :param x: float:
        :param y: float:
        :return: Calc.last_result = x * y
        """
        self.last_result = x * y
        return self.last_result

    def division_operation(self, x: float, y: float):
        """
        :param x: float:
        :param y: float:
        :return: Calc.last_result = x / y
        """
        if y != 0:
            self.last_result = x / y
            return self.last_result
        else:
            self.last_result = "division by zero."
            return self.last_result


s = Calc()
s.division_operation(7, 0)
print(s.last_result)
s.division_operation(7, 2)
print(s.last_result)
