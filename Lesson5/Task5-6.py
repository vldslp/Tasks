with open('Task5-6.txt', encoding='utf-8') as inf_obj:
    for line in inf_obj:
        inf_list = line.split()
        dis = inf_list[0].removesuffix(':')
        l = [int(i.removesuffix('(л)')) for i in inf_list if '(л)' in i]
        pr = [int(i.removesuffix('(пр)')) for i in inf_list if '(пр)' in i]
        lb = [int(i.removesuffix('(лаб)')) for i in inf_list if '(лаб)' in i]
        dis_d = {dis: sum(l + pr + lb)}
        print(dis_d)
