# Задача 4 к первому занятию
a = input('Введите многозначное положительное целое число -> ')
y = len(a)
a = int(a)
i = 1
e = a
v = a
m = 0
while i <= y:
    c = e // 10
    d = e - c * 10
    e = c
    n = 1
    while n <= y:
        f = v // 10
        g = v - f * 10
        v = f
        if d <= g and m < g:
            m = g
        elif m < d:
            m = d
        n += 1
    v = a
    i += 1
print("Самая большая цифра в числе:", m)
