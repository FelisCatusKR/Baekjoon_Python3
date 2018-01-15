# 2156.py
N = int(input())
wineVolume = [int(input())for _ in range(N)]
totalVolume = []

for i in range(N):
    # 첫 번째 잔까지의 최댓값: 첫 번째 잔의 포도주의 양
    if i == 0:
        totalVolume.append(wineVolume[i])
    # 두 번째 잔까지의 최댓값: 첫 번째 잔 + 두 번째 잔의 포도주의 양
    elif i == 1:
        totalVolume.append(wineVolume[i] + totalVolume[i-1])
    # 세 번째 잔까지의 최댓값: 1+2, 1+3, 2+3 중 최댓값
    elif i == 2:
        totalVolume.append(max(totalVolume[i-1], wineVolume[i] + totalVolume[i-2],
                               wineVolume[i] + wineVolume[i-1]))
    # i번째부터는 세 가지 경우 중 최댓값을 반영
    else:
        totalVolume.append(max(totalVolume[i-1], wineVolume[i] + totalVolume[i-2],
                               wineVolume[i] + wineVolume[i-1] + totalVolume[i-3]))

print(totalVolume[-1])