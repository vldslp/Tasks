from itertools import cycle, count

i = 0
a_list = []
for i in count(15, 3):
    if i < 100:
        a_list.append(i)
    else:
        break
print(a_list)
# ---------------------------
b_list = []
x = ['Да', 'Нет', 'Не знаю']
for y in cycle(x):
    if len(b_list) < 50:
        b_list.append(y)
    else:
        break
print(b_list)
