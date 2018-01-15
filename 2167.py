# 2167.py
matrix = []
N, M = map(int, input().split())
for i in range(N):
    matrix.append(list(map(int, input().split())))
for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    s = 0
    for a in range(i-1, x):
        s += sum(matrix[a][(j-1):y])
    print(s)