def get_num_hexagons():
    n = input('Введите количество шестиугольников, располагаемых в ряд, в диапазоне от 4 до 20: ')
    k = 0
    while k < 1:
        try:
            if 4 <= int(n) <= 20:
                k += 1
                return int(n)
            else:
                print('Введено некорректное значение. Повторите попытку: ')
                n = input('Введите количество шестиугольников, располагаемых в ряд, в диапазоне от 4 до 20: ')
        except ValueError:
            print('Введено некорректное значение. Повторите попытку: ')
            n = input('Введите количество шестиугольников, располагаемых в ряд, в диапазоне от 4 до 20: ')


N = get_num_hexagons()

d = 500 / (N + 0.5)

from turtle import *

lngth = -250 + k/2
wdth = 250

for i in range(N):
    for j in range(N):
        draw_hexagon(lngth, wdth, k, color1)



