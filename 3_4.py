"""
3. Напишіть програму, де клас «геометричні фігури» (figure) містить властивість color з початковим значенням white
    і метод для зміни кольору фігури, а його підкласи «овал» (oval)
    і «квадрат» (square) містять методи __init__ для завдання початкових розмірів об'єктів при їх створенні.

4. Видозмініть програму так, щоб метод __init__ мався в класі «геометричні фігури» та приймав кольор фігури
    при створенні екземпляру, а методи __init__ підкласів доповнювали його та додавали початкові розміри
"""


class Figure(object):
    color: str = "white"

    def color_change_operation(self, color: str):
        Figure.color = color
        return Figure.color


class Oval(Figure):
    def __init__(self, x_h: float, y_w: float):
        self.x_h = x_h
        self.y_w = y_w


class Square(Figure):
    def __init__(self, x: float):
        self.x = x
o = Oval(5,10)
print(o.color)
s = Square(5)
print(s.color)

# 4. ************************************************************************
print("4. " + "*" * 50)

class FigureMod(object):
    def __init__(self, color: str):
        self.color = color


class OvalMod(FigureMod):
    def __init__(self, x_h: float, y_w: float, color: str = "white"):
        FigureMod.__init__(self, color)
        self.x_h = x_h
        self.y_w = y_w


class SquareMod(FigureMod):
    def __init__(self, x: float, color: str = "white"):
        FigureMod.__init__(self, color)
        self.x = x


o = OvalMod(5, 10, "red")
print(o.color)
s = SquareMod(5, "BLACK")
print(s.color)
s_1 = SquareMod(7)
print(s_1.color)

