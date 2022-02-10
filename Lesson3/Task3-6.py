def int_func():
    sl = ''
    slv = list(input('Введите слова через пробел: ').split())
    for i in range(len(slv)):
        sl = ' '.join([sl, (slv[i].capitalize())])
    print(sl)


int_func()
