class Worker:
    def __init__(self, n, s, p, w, b):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {'wage': w, 'bonus': b}


class Position(Worker):
    def dat(self, n, s, p, w, b):
        Worker._income = {'wage': w, 'bonus': b}
        print('Фамилия, Имя:', s + ' ' + n)
        print(f'Должность: {p}')
        print(f'Полный доход: {Worker._income["wage"] + Worker._income["bonus"]} руб.')


fio = Position('Иван', 'Петров', 'инженер', 53000, 11500)
fio.dat('Иван', 'Петров', 'инженер', 53000, 11500)
print('-' * 30)
print(fio.position + ' ' + fio.surname + ' ' + fio.name)
print(type(fio._income))
