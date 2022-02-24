from abc import ABC, abstractmethod


class Wear(ABC):
    def __init__(self):
        self.cl1 = 0
        self.cl2 = 0

    @abstractmethod
    def cloth(self, p):
        pass

    def __add__(self, other):
        return f'Промежуточный расход ткани: {round(self.cl1 + other.cl2, 2)} м'


class Suit(Wear):
    def cloth(self, p):
        self.cl1 = p * 2 + 0.3
        return self.cl1

    @property
    def p(self):
        return f'Для костюма: {round(self.cl1, 2)} м'


class Coat(Wear):
    def cloth(self, p):
        self.cl2 = p / 6.5 + 0.5
        return self.cl2

    @property
    def p(self):
        return f'Для пальто: {round(self.cl2, 2)} м'


a = Suit()
b = Coat()
d = a.cloth(1.84)
e = b.cloth(54)
print(a.p)
print(b.p)
print(a + b)
f = a.cloth(1.70)
g = b.cloth(50)
print(a.p)
print(b.p)
print(a + b)
print('Общий расход ткани', round(d + e + f + g, 2), 'м')
