# Задача 3 ко второму занятию
mo = int(input('Введите номер месяца: '))
se = ['зима', 'весна', 'лето', 'осень']
if mo <= 2 or mo == 12:
    print('На дворе', se[0])
elif mo <= 5:
    print('На дворе', se[1])
elif mo <= 8:
    print('На дворе', se[2])
elif mo <= 11:
    print('На дворе', se[3])
