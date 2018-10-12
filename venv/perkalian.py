m1 = [
    [5, 0],
    [2, 6],
    ]

m2 = [
    [1, 0],
    [4, 2],
    ]
m3 = []

for x in range(0, len(m1)):
    row = []
    for y in range(0, len(m1[0])):
        total = 0
        for z in range(0, len(m1)):
            total = total + (m1[x][z] * m2[z][y])
            row.append(total)
            m3.append(row)
            for x in range(0, len(m3)):
                for y in range(0, len(m3[0])):
                    print(m3[x][y], end=''),print(total)
