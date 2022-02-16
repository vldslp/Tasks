from random import random

with open('Task5-5.txt', 'w', encoding='utf-8') as f:
    num_l = [round(random() * 100, 3) for i in range(15)]
    num_l = str(num_l).split(',')
    f.writelines(num_l[1:len(num_l) - 1:])

with open('Task5-5.txt') as f:
    s_l = f.readline().split(' ')
    s_l = [float(i) for i in s_l if i != '']
    print('Ряд чисел:', s_l)
    print('Сумма ряда:', round(sum(s_l), 3))