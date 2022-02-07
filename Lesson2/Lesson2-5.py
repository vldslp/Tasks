# Задача 5 ко второму занятию
r = [10, 8, 7, 5, 2, 1]
c = int(input('Введите натуральное число от 1 до 10: '))
for i in r:
    if c > i:
        y = r.index(i)
        r.insert(y, c)
        break
    if c == i:
        y = 1 + r.index(i)
        r.insert(y, c)
        break
print(f"Рейтинг:{r}")
