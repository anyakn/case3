from turtle import *
from math import *

def draw_hexagon(x, y, side_len, color):
    pu()
    goto(x, y)
    pd()
    fillcolor(color)
    begin_fill()

    angle = 60
    side_len = side_len / cos(radians(angle/2))
    for i in range(6):
        fd(side_len)
        rt(angle)

    end_fill()
    pu()

exitonclick()
#draw_hexagon(-300,300, 120, 'black')



'''
x, y = map(int, input('Введите координаты точки, от которой рисуется фигура: ').split())
side_len = int(input('Введите длину стороны шестиугольника: '))
color = input('Введите название цвета для фигуры: ')
draw_hexagon(x, y, side_len, color)
'''