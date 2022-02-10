def sum_func():
    s = 0
    rs = 0
    k = ''
    while k != 'q':
        k = str(input('Для выхода нажмите "Q", чтобы продолжить - "enter":'))
        if k != 'q':
            ch = list(input('Введите числа через пробел:').split())
            for i in range(len(ch)):
                if ch[i] == 'q':
                    rs = rs + s
                    print("-" * 55)
                    print(f'Сумма:\n  текущая {s}\n  накопительная {rs}')
                    print("-" * 55)
                    return
                elif ch[i].isdigit():
                    s = s + float(ch[i])
                else:
                    break
            rs = rs + s
            print("-" * 55)
            print(f'Сумма:\n  текущая {s}\n  накопительная {rs}')
            print("-" * 55)
            s = 0
        else:
            break


sum_func()
