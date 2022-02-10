def sm_func(a_1, a_2, a_3):
    a_min = min(a_1, a_2, a_3)
    ss = 0
    a = [a_1, a_2, a_3]
    b = [0, 1, 2]
    for i in range(3):
        if a[i] == a_min:
            c = b.pop(i)
            for c in b:
                ss = ss + a[c]
    print(f'Сумма двух наибольших чисел =', ss)


sm_func(12, 0.2, -15)
