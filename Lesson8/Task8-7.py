class Kmpl:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        print(self.x[0], other.x[0])
        sum = [self.x[0] + other.x[0], self.x[1] + other.x[1]]
        print(f'Результат сложения: {sum[0]}{"+" + str(sum[1]) if sum[1] > 0 else ""}j')

    def __mul__(self, other):
        prv = [self.x[0] * other.x[0] - self.x[1] * other.x[1],
               self.x[0] * other.x[1] + self.x[1] * other.x[0]]
        print(f'Результат умножения: {prv[0]}{"+" + str(prv[1]) if prv[1] > 0 else ""}j')


a = Kmpl([3, 5])
b = Kmpl([-3, 10])

a + b
print(complex(3, 5) + complex(-3, 10))
a * b
print((3 + 5j) * (-3 + 10j))
