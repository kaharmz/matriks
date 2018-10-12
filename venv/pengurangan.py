A = [
    [5, 0],
    [2, 6],
]

B = [
    [1, 0],
    [4, 2],
]

for x in range(0, len(A)):
    for y in range(0, len(A[0])):
        print(A[x][y] - B[x][y], end=''), print()