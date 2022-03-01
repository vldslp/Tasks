class Data:
    def __init__(self, dat):
        self.dat = dat
        self.izv(dat)

    @classmethod
    def izv(cls, d_m_y):
        cls.val([int(i) for i in str(d_m_y).split('-')])

    @staticmethod
    def val(dt):
        print(f'День: {dt[0]}') if dt[0] in range(1, 32) else print('Введите день правильно')
        print(f'Месяц: {dt[1]}') if dt[1] in range(1, 13) else print('Введите месяц правильно')
        print(f'Год: {dt[2]}') if dt[2] // 100 > 0 else print('Введите год правильно')


z = Data('32-35-20')
y = Data('01-01-2001')
