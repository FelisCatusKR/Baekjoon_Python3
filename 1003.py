# 1003.py
calledTime = [[1, 0], [0, 1]]
N = int(input())
n = []
for _ in range(N):
    n.append(int(input()))
for i in range(2, max(n)+1):
    calledTime.append([calledTime[i-2][0] + calledTime[i-1][0],
                       calledTime[i-2][1] + calledTime[i-1][1]])
for i in range(N):
    print(calledTime[n[i]][0], calledTime[n[i]][1])