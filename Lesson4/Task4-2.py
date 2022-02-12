sp_l = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
res_l = [sp_l[i] for i in range(0, len(sp_l)) if i > 0 and sp_l[i - 1] < sp_l[i]]

print(res_l)
