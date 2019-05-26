# Напечатать таблицу Пифагора заданной конфигурации.
# Образец: https://cdn.lifehacker.ru/wp-content/uploads/2017/01/700_1485755264.jpg

i = 0
while i <= 10:
    j = 0
    while j <= 10:
        if i+j == 0:
            print('\t', end='')
        elif i*j == 0:
            print('\t', i+j, end='')
        else:
            print('\t', i*j, end='')
        j += 1
    print()
    i += 1
