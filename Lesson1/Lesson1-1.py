# Задача 1 к первому занятию
a = str('Вас зовут')
b = str('Добрый день!\n')
d = input('Введите ваше имя: ')
c = input('Введите ваш возраст: ')
e = int(c) // 10
f = int(c) % 10
print(b + a, d + '!')
print('Вам', e * 10 + f, 'лет.')
