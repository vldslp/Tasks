class Car:
    def __init__(self, s, c, n, cd):
        self.speed = s
        self.color = c
        self.name = n
        self.cud = cd

    def go(self):
        print(f'{self.color} {self.name} тронулся(ась)')

    def stop(self):
        print(f'{self.color} {self.name} останавливается')

    def turn(self):
        print(f'{self.name} поехал(а) {self.cud}')

    def show_speed(self, s):
        print(f'Текущая скорость {self.name} {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, s, c, n, p, cd):
        super().__init__(s, c, n, cd)
        self.is_police = p
        print('Это полиция') if p is True else print('Гражданская машина')

    def show_speed(self, s):
        self.speed = s
        print(f'Текущая скорость {self.name} {s} км/ч')
        print(f'Скорость превышена на {s - 60} км/ч') if s > 60 else ''


class SportCar(Car):
    def __init__(self, s, c, n, p, cd):
        super().__init__(s, c, n, cd)
        self.is_police = p
        print('Это полиция') if p is True else print('Гражданская машина')


class WorkCar(Car):
    def __init__(self, s, c, n, p, cd):
        super().__init__(s, c, n, cd)
        self.is_police = p
        print('Это полиция') if p is True else print('Гражданская машина')

    def show_speed(self, s):
        print(f'Текущая скорость {self.name} {s} км/ч')
        print(f'Скорость превышена на {s - 40} км/ч') if s > 40 else ''


class PoliceCar(Car):
    def __init__(self, s, c, n, p, cd):
        super().__init__(s, c, n, cd)
        self.is_police = p
        print('Это полиция')


t = TownCar(65, 'красная', 'Лада', False, 'прямо')
t.go()
t.turn()
t.show_speed(70)
print("-" * 30)

a_t = PoliceCar(65, 'белый', 'Форд', True, 'налево')
a_t.show_speed(45)
a_t.turn()
a_t.stop()
print(a_t.speed)
print("-" * 30)
