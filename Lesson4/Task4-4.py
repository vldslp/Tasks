n_l = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
res_l = [n_l[i] for i in range(0, len(n_l)) if n_l.count(n_l[i]) == 1]
print(res_l)
