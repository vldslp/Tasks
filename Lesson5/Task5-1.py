with open('Task5-1.txt', 'w') as t_list:
    while True:
        with open('Task5-1.txt', 'a') as t_list:
            a = input('Введите текст: ')
            if a == '':
                with open('Task5-1.txt') as t_list:
                    print(f'вот что получилось:')
                    for line in t_list:
                        print(line, end="")
                break
            t_list.writelines(a + '\n')