from turtle import *
def get_color_choice():
    colors = ['оранжево-красный', 'кораловый', 'кадетский-синий', 'тёмно-аспидный синий',
              'бледно-зелёный', 'светло-коричневый']
    codes = ['orangered', 'coral', 'cadetblue', 'darkslategray', 'powderblue', 'mocasin']

    print('Допустимые цвета заливки:', 'оранжево-красный', 'кораловый', 'кадетский-синий', 'тёмно-аспидный синий',
          'бледно-зелёный', 'светло-коричневый', sep='\n')

    first_one = ''
    chosen_one = input('Пожалуйста, выберете цвет: ').lower()

    while first_one == '':
        for idx in range(6):
            if chosen_one in colors:
                idx = colors.index(chosen_one)
                first_one = codes[idx]
            else:
                print(chosen_one, 'не является верным значением')
                chosen_one = input('Пожалуйста, повторите попытку: ').lower()

    second_one = ''
    chosen_two = input('Пожалуйста, выберете цвет: ').lower()

    while second_one == '':
        for idx in range(6):
            if chosen_two in colors:
                idx = colors.index(chosen_two)
                second_one = codes[idx]
            else:
                print(chosen_two, 'не является верным значением')
                chosen_two = input('Пожалуйста, повторите попытку: ').lower()

    return first_one, second_one

first_color, second_color = get_color_choice()