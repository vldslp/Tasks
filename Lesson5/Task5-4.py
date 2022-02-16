with open('Task5-4in.txt', encoding='utf-8') as t_obj:
    n_list, m_list = [], []
    ch_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    i = 0
    for line in t_obj:
        n_list = line.split()
        for y in ch_dict:
            if n_list[0] in y:
                n_list[0] = ch_dict.get(y)
                n_list = ' '.join(n_list) + '\n'
                m_list.extend(n_list)
                break

with open('Task5-4out.txt', 'w', encoding='utf-8') as out_obj:
    out_obj.writelines(m_list)
