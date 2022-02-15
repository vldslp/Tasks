with open('Task5-2.txt') as st:
    i = 0
    for line in st:
        line = line.split()
        y = ' '.join(line).count(' ') + 1
        line_2 = []
        for el in line:
            line_2.append(el.strip())
        i += 1
        print(f'Слов в строке = {str(y)}:', ' '.join(line_2))
    print(f'Cтрок в тексте = {i}')
