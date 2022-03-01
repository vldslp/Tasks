class Sklad:
    def __init__(self, emk=100):
        self.emk = emk  # Емкость склада

    def uchet(self, podr, ed):
        self.podr = podr
        self.ed = ed
        summ = len(Printer.prt) + len(Scaner.scn) + len(Xerox.xrx)
        print(summ)


class Org:
    def __init__(self, brand, price, kol):
        self.kol = kol
        self.price = price
        self.brand = brand


class Printer(Org):
    def __init__(self, brand, price, kol, clr):
        super().__init__(brand, price, kol)
        self.clr = clr  # Цвет принтера

    def zpl(self, kol=1):  # Заполнение однотипных позиций
        prt = []
        for i in range(kol):
            prt.append(Printer(self.brand, self.price, self.kol, self.clr))


class Scaner(Org):
    def __init__(self, brand, price, kol, tp):
        super().__init__(brand, price, kol)
        self.tp = tp  # Тип сканера

    def zpl(self, kol=1):  # Заполнение однотипных позиций
        scn = []
        for i in range(kol):
            scn.append(Scaner(self.brand, self.price, self.kol, self.tp))


class Xerox(Org):
    def __init__(self, brand, price, kol, v_lot):
        super().__init__(brand, price, kol)
        self.v_lot = v_lot  # Объем лотка под бумагу

    def zpl(self, kol=1):  # Заполнение однотипных позиций
        xrx = []
        for i in range(kol):
            xrx.append(Xerox(self.brand, self.price, self.kol, self.v_lot))


p = Printer

p1 = Printer('Epson', 5600, 11, 'черный')
p2 = Printer('HP', 7700, 13, 'белый')
p3 = Printer('Oki', 10600, 5, 'серый')
s1 = Scaner('Plustek', 12500, 15, 'книжный')
s2 = Scaner('Canon', 19000, 10, 'протяжный')
s3 = Scaner('Mustek', 5700, 8, 'ручной')
x1 = Xerox('Canon', 16100, 12, 500)
x2 = Xerox('Xerox', 35000, 9, 1500)
x3 = Xerox('Kyocera', 28000, 12, 1000)

print(Sklad.uchet("Бухгалерия", 5))
