def fio_func(name='', family='', born='', sity='', mail='', tel=''):
    print(f'{name} {family}, {born} г.р., г.{sity}, e-mail:{mail}, тел.{tel}')


fio_func(name='Вася',
         family='Петров',
         tel='+79991112233',
         sity='Рио-де-Житомир',
         born='1980',
         mail='pet@pet.com')
