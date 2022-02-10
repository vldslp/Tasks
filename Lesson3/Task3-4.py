def st_func(x, y):
    c = 1
    for i in range(abs(y)):
        c = c * x
    print(f'Результат возведения в степень: \n  Использование "**":    ', round(x ** y, 6))
    print('  Без использования "**":', round(1 / c, 6))


st_func(20, -3)
