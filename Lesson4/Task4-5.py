from functools import reduce


def m_func(prev_el, el):
    return prev_el * el


my_list = [i for i in range(100, 1001, 2)]
p = str(reduce(m_func, my_list))
n = 10  # Количество знаков после запятой
pr = int(p[:n+1:]) / 10**(n)
print(f'{pr}e+{len(p)}')
