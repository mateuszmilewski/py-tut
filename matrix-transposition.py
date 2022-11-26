m = [
    [1,2,3,4],
    [8,7,6,5],
    [11,12,13,14]
]


tm1 = [[row[i] for row in m] for i in range(4) ]

tm2 = []
for i in range(4):
    tm2.append([row[i] for row in m])

print(' m ', m, ' tm1 ', tm1, ' tm2 ' ,tm2)