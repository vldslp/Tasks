# Задача 5 к первому занятию
v = float(input('Выручка фирмы, тыс.руб.: '))
iz = float(input('Издержки фирмы, тыс.руб.: '))
ch = int(input('Численность сотрудников фирмы, чел.: '))
if v > iz:
    rent = (v - iz) / v
    rent = float('{:.3f}'.format(rent))
    chi = (v - iz) / ch
    chi = float('{:.3f}'.format(chi))
    print("Фирма рентабельна")
    print("Рентабельность", rent)
    print(f"Прибыль на одного сотрудника {chi}, тыс.руб.")
elif v < iz:
    print("Фирма нерентабельна")
else:
    print("Фирма имеет нулевой баланс")
