with open('Task5-3.txt', encoding='utf-8') as b_obj:
    sr = 0
    zz = []
    for line in b_obj:
        zp = line.split()
        for el in zp:
            zz.append(el.strip())
    for i in range(1, len(zz) + 1, 2):
        sr += float(zz[i])
        if float(zz[i]) < 20000:
            print(zz[i - 1])
print('Средний оклад, руб.:', round((sr / (len(zz) / 2)), 2))
