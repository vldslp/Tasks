class TrifficLight:
    __color = ''
    clr = ['красный', 'желтый', 'зеленый']
    while __color not in clr:
        __color = (input('Смена цветов светофора. С какого начать?\n'
                         'Введите "красный", "желтый" или "зеленый": ')).lower()

        def running(self):
            cc = int(input('Количество циклов: '))
            cy = cc * 3 if cc == 1 else cc * 3 + 1
            ti = [7, 2, 5]
            c = 0
            from time import sleep
            t = sum([v for v, n in enumerate(self.clr) if n == self.__color])
            while True:
                if t < 3:
                    print(f'--> {self.clr[t].upper()} <--  Смена через {ti[t]}с')
                    sleep(ti[t])
                    t += 1
                    c += 1
                else:
                    t = 1
                    self.clr = self.clr[::-1]
                    ti = ti[::-1]
                if c > cy:
                    if (input('Для выхода - "space", продолжить работу - "enter": ')).upper() != ' ':
                        cc = int(input('Количество циклов: '))
                        cy = cc * 3 if cc == 1 else cc * 3 + 1
                        c = 0
                    else:
                        break


s = TrifficLight()
s.running()
