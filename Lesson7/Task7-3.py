class Cell:
    def __init__(self, q, n):
        self.q = q
        self.n = n

        if self.q < 0:
            raise 'Введите положительные целые числа!'

    def __add__(self, other):
        dc = self.q + other.q
        print(f'Сумма клеток: {dc}')
        self.make_order(dc, self.n)

    def __sub__(self, other):
        dc = self.q - other.q
        print(f'Разница клеток: {dc}')
        self.make_order(dc, self.n)

    def __mul__(self, other):
        dc = self.q * other.q
        print(f'Произведение клеток: {dc}')
        self.make_order(dc, self.n)

    def __truediv__(self, other):
        dc = self.q // other.q
        print(f'Деление клеток нацело: {dc}')
        self.make_order(dc, self.n)

    def make_order(self, c, n):
        o = ''
        self.c = c
        self.n = n
        c = self.c // self.n
        for i in range(c):
            o += '*' * self.n + '\n'
        print(o + '*' * (self.c - c * self.n))
        print('-' * 20)


a = Cell(9, 6)
b = Cell(8, 3)
print('Исходные клетки:')
a.make_order(9, 6)
b.make_order(8, 3)
a + b
a - b
a * b
a / b
