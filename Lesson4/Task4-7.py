def fact():
    global m
    m = int(input('Введите значение факториала: '))
    for i in range(1, m + 1):
        r = i
        yield r


res = 1
n = fact()
for y in n:
    res = res * y
print(f'{m}! = {res}')
