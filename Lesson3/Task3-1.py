def d_func(d_1, d_2):
    while True:
        if d_2 != 0:
            print(f'Результат деления: {d_1 / d_2}')
            break
        else:
            d_2 = float(input('Введите делитель дроби отличный от нуля: '))


d_func(2, 0)
