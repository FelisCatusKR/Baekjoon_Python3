# 2193.py
N = int(input())
if N < 3:
    print(1)
else:
    n = [0, 1, 1]
    for i in range(3, N+1):
        n.append(n[i-2] + n[i-1])
    print(n[N])
