# 2579.py
N = int(input())
stepScore = [0]
for _ in range(N):
    stepScore.append(int(input()))
totalScore = [0]
for i in range(1, N + 1):
    if i <= 2:
        totalScore.append(stepScore[i] + totalScore[i - 1])
#   elif i == 3:
#       totalScore.append(max(stepScore[i] + totalScore[i - 2],
#                             stepScore[i] + stepScore[i - 1]))
    else:
        totalScore.append(max(stepScore[i] + totalScore[i - 2],
                              stepScore[i] + stepScore[i - 1] + totalScore[i - 3]))
print(totalScore[N])