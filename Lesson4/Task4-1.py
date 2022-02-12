from sys import argv

_, th, nt, pr = argv
try:
    zp = float(th) * float(nt) + float(pr)
    print('Зарплата составит: ', zp)
except:
    print('Введите положительные числа через пробел: \nВыработка--часовая ставка--премия')
