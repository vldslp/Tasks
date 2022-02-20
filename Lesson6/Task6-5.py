class Stationery:
    def __init__(self, t):
        self.title = t

    def draw(self):
        print(f'Взяли в руку {self.title} - начинаем рисовать.')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} пишет')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} рисует')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} подчеркивает')


a = Pen('Ручка')
a.draw()

b = Pencil('Карандаш')
b.draw()

c = Handle('Маркер')
c.draw()

d = Stationery('Рапидограф')
d.draw()
