# 1010.py
factorial = [1]
for _ in range(int(input())):
    N, M = map(int, input().split())
    if M > len(factorial)-1:
        for i in range(len(factorial), M+1):
            factorial.append(factorial[i-1] * i)
    print(factorial[M] // (factorial[M - N] * factorial[N]))