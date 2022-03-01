class Inp:
    def __init__(self, a=None):
        self.a = a
        sps = []
        while True:
            self.a = input('Введите число:')
            if self.a != 'stop':
                if str(self.a).replace('-', '').replace('.', '').isdigit():
                    sps.append(float(self.a))
                else:
                    print(f'{self.a} - не является числом! ', end='')
                    Ex()
            else:
                print(sps)
                break


class Ex(Exception):
    def __init__(self):
        print('Введите значение правильно!')
        return


d = Inp()
