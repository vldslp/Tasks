# Задача 2 ко второму занятию
base = (input('Введите через запятую элементы списка: ')).split(",")
fin = []
e1 = base[::2]  # нечетные
e2 = base[1::2]  # четные
i = 1
for y in e1:
    e2.insert(i, y)
    if i < len(base):
        i = i + 2
print(e2)
