with open('Task5-7in.txt', encoding='utf-8') as com_obj:
    p_l = []
    pr_l = []
    sum_l = []
    i = 1
    for line in com_obj:
        in_l = line.split()
        prib = int(in_l[2]) - int(in_l[3])
        p_l.append([in_l[0], prib])
        if prib > 0:
            sum_l.append(prib)
            i += 1
    aver = round(sum(sum_l) / (i - 1), 2)
    summary = [dict(p_l), {'Average profit': aver}]
    print(summary)

import json

with open('Task5-7out.json', 'w', encoding='utf-8') as out_jsn:
    json.dump(summary, out_jsn)
