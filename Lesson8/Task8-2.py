class Div:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        if str(self.a).replace('-', '').replace('.', '').isdigit() is True \
                and str(self.b).replace('-', '').replace('.', '').isdigit() is True:
            self.div()
        else:
            Ex()


    @classmethod
    def div(cls):
        if b == 0:
            print(f'Деление на ноль!')
            Ex()
        else:
            c = float(a) / float(b)
            print(f'а / b = {c}'+'\n'+'-'*20)


class Ex(Exception):
    def __init__(self):
        print(f'Введите числа правильно!\na / b = {a} / {b}'+'\n'+'-'*20)


a = -10
b = 20
v = Div(a, b)

a = 10
b = 0
v = Div(a, b)

a = '10'
b = 4
v = Div(a, b)

a = 10
b = 'b'
v = Div(a, b)