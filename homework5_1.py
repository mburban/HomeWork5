# Случайным образом программа выбирает целое число от 1 до 10 и предлагает пользователю его угадать.
# Пользователь вводит число, а программа проверяет его и, если пользователь не угадал, то говорит больше или меньше.
# После чего опять просит угадать. И так пока пользователь не угадает выбранное число.

from random import randint
random_number = randint(1, 10)
input_number = 0
while random_number != input_number:
    input_number = int(input('Введите число: '))
    if input_number > random_number:
        print('Загаданное число меньше.')
    elif input_number < random_number:
        print('Загаданное число больше.')
    else:
        print('Угадали.')
