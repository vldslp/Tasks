# Входящий на склад товар (Приход.txt) получает инвентарный номер и
# поступает на склад (Склад.txt).
# Далее обрабатывается заявка на оборудование из отделов(Заявка.txt)
# Формируется ведомость передачи на баланс техники в отдел (баланс.txt).
# Товар изымается со склада (Склад.txt).
with open('Склад.txt', 'w', encoding='utf-8') as _:
    _.writelines('')


class Sklad:
    def __init__(self, emk=500):
        self.emk = emk  # Емкость склада

    inv = 1
    dev = []

    def uchet(self):
        d = []
        zv = Sklad.zajavka()
        scl = Sklad.dev
        for m in zv:
            n = 0
            v = 0
            while n < int(m[-1]) and v < len(scl):
                if scl[v].count(m[1]) and scl[v].count(m[2]):
                    scl[v].insert(0, m[0])
                    d.append(scl[v])
                    scl.remove(scl[v])
                    v -= 1
                    n += 1
                v += 1
        if len(scl) < self.emk:
            print(f'Склад заполнен на {len(scl)} из {self.emk} позиций')
        else:
            Ex(len(scl), self.emk)
        Sklad.vyvod('Баланс.txt', d, 'w+')
        Sklad.vyvod('Склад.txt', scl, 'w+')
        Sklad.blns(d)

    @staticmethod
    def blns(d):
        balans = []
        param, klv, p_list = [0, 0, 0], [0, 0, 0], [0, 0, 0]
        otd = ['Бухгалтерия', 'Техотдел', 'Сервис']
        tv = ['printer', 'scaner', 'copier']
        j = 0
        for i in d:
            for e, y in enumerate(otd):
                p_list[e] += 1 if i[0] == y else 0
        for i in range(len(p_list)):
            while j < p_list[i]:
                for q, k in enumerate(tv):
                    if d[j][1] == k:
                        param[q] += d[j][3]
                        klv[q] += 1
                balans.append([otd[i], param, klv]) if j == p_list[i] - 1 else None
                j += 1
            else:
                d = d[p_list[i]:]
                i += 1
                j = 0
                param, klv = [0, 0, 0], [0, 0, 0]

        zv = Sklad.zajavka()
        y = 0
        for i in range(0, len(zv), 3):
            balans[y].append([zv[i][3], zv[i + 1][3], zv[i + 2][3]])
            y += 1

        print('Балансовая ведомость переданных позиций:'.center(62, '-'))
        for i in balans:
            print(f'{i[0]}:')
            for j in range(len(i[2])):
                zz = f"Заявка удовлетворена" if (i[2][j] - i[3][j]) >= 0 \
                    else f"Дефицит {abs(i[2][j] - i[3][j])} ед."
                print(f'{tv[j]}\t\t{i[1][j]} руб.\t\t{i[2][j]} ед.\t\t', zz)
            print('-' * 62)

    @classmethod
    def inven(cls, t):  # Инвентарный номер
        d = []
        for i in range(t[-1]):
            dv = t[:-1:]
            dv.append('Инв.№' + str(cls.inv))
            cls.inv += 1
            d.append(dv)
        Sklad.vyvod('Склад.txt', d, 'a')
        cls.dev.extend(d)
        return cls.dev

    @staticmethod
    def vvod(file_obj, out):  # Чтение из файла
        t = []
        with open(file_obj, encoding='utf-8') as in_obj:
            for line in in_obj:
                k = line[:-1].split(';') if line[-1] == '\n' else line.split(';')
                for i, u in enumerate(k):
                    k[i] = int(u) if u.replace('-', '').replace('.', '').isdigit() else str(u)
                Sklad.inven(k) if out == 'yes' else ''
                t.append(k)
        return t

    @staticmethod
    def vyvod(file_obj, dev, mtd):  # Вывод в файл
        ot = ''
        for y in dev:
            for z in y:
                ot += str(z) + ';'
            ot = ot[:-1:] + '\n'
        with open(file_obj, mtd, encoding='utf-8') as _:
            _.writelines(str(ot))

    @staticmethod
    def prihod():
        file_obj = 'Приход.txt'
        out = 'yes'
        pr = Sklad.vvod(file_obj, out)
        return pr

    @staticmethod
    def zajavka():
        file_obj = 'Заявка.txt'
        out = ''
        zv = Sklad.vvod(file_obj, out)
        return zv


class Org:
    def __init__(self, typ, brand, price, kol):
        self.kol = kol
        self.price = price
        self.brand = brand
        self.typ = typ


class Printer(Org):
    def __init__(self, typ, brand, price, param, kol):
        super().__init__(typ, brand, price, kol)
        self.clr = param  # Цвет принтера
        self.t = [typ, brand, price, param, kol]
        Sklad.inven(self.t)


class Scaner(Org):
    def __init__(self, typ, brand, price, param, kol):
        super().__init__(typ, brand, price, kol)
        self.tp = param  # Тип сканера
        self.tp = [typ, brand, price, param, kol]
        Sklad.inven(self.tp)


class Copier(Org):
    def __init__(self, typ, brand, price, param, kol):
        super().__init__(typ, brand, price, kol)
        self.lot = param  # Объем лотка под бумагу
        self.lot = [typ, brand, price, param, kol]
        Sklad.inven(self.lot)


class Ex(Exception):
    def __init__(self, scl, emk):
        # self.scl = scl
        # self.emk = emk
        print(f'Не хватает {scl - emk} позиций на складе!')
        return


p = Printer
s = Scaner
c = Copier

# Исходное состояние склада:
# <Тип>-<Бренд>-<Цена>-<Уник.парам.>-<количество>
p('printer', 'Epson', 6000, 'черный', 11)
p('printer', 'Lexmark', 9700, 'белый', 13)
p('printer', 'Oki', 10500, 'серый', 5)
s('scaner', 'Epson', 12500, 'книжный', 1)
s('scaner', 'Canon', 19000, 'протяжный', 3)
s('scaner', 'HP', 3700, 'ручной', 4)
c('copier', 'Ricoh', 16100, 500, 12)
c('copier', 'Samsung', 35000, 1500, 9)
c('copier', 'Panasonic', 28000, 1000, 12)

# Оформляем приход товара на склад с присвоением инв.номера:
Sklad.prihod()
# Принимаем заявку отделов:
Sklad.zajavka()

# Обрабатываем заявку отделов:
Sklad().uchet()
# Поступление техники на баланс отделов выводим в Баланс.txt
# Балансовая ведомость выводится на экран.
