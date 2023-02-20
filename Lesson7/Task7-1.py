class Matrix:
    def __init__(self, mtr):
        self.mtr = mtr
        self.n = []
        self.p = []
        self.s = []

    def __str__(self):
        for i in self.mtr:
            self.n.append(str(i).replace(',', '  ').removeprefix('[').removesuffix(']'))
        return "\n".join(self.n) + f"\n{'-' * 15}"

    def __add__(self, other):
        d = len(self.mtr) - len(other.mtr)
        if d > 0:
            j = len(other.mtr) + 1
            for j in range(d):
                ad = [h * 0 for h in self.mtr[j + len(other.mtr)]]
                other.mtr.append(ad)
        elif d < 0:
            j = len(self.mtr) + 1
            for j in range(abs(d)):
                ad = [h * 0 for h in other.mtr[j + len(self.mtr)]]
                self.mtr.append(ad)
        for y, m in enumerate(self.mtr):
            self.s.append(list(map(lambda x, y: x + y, m, other.mtr[y])))
        for i in self.s:
            self.p.append(str(i).replace(',', '  ').removeprefix('[').removesuffix(']'))
        return "\n".join(self.p) + f"\n{'-' * 15}"


a = Matrix([[1, 2, 4], [3, 4, 5], [5, 6, 6]])
b = Matrix([[11, 22, 44], [10, 20, 30]])
print(a)
print(b)
print(f'Результат сложения матриц:\n{a + b}')
