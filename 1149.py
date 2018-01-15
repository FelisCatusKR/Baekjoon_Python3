# 1149.py
def calcCost(priceList, color, n, N):
    # 재귀의 끝에 도달한 경우 마지막 집의 색칠 비용을 리턴
    if n == N:
        if color == 'R':
            return priceList[n-1][0]
        elif color == 'G':
            return priceList[n-1][1]
        elif color == 'B':
            return priceList[n-1][2]
    # 현재 단계의 집과 다른 색깔을 칠한 후 최솟값을 구하는 재귀 함수 구현
    else:
        if color == 'R':
            return min(priceList[n-1][0] + calcCost(priceList, 'G', n+1, N),
                       priceList[n-1][0] + calcCost(priceList, 'B', n+1, N))
        elif color == 'G':
            return min(priceList[n-1][1] + calcCost(priceList, 'R', n+1, N),
                       priceList[n-1][1] + calcCost(priceList, 'B', n+1, N))
        elif color == 'B':
            return min(priceList[n-1][2] + calcCost(priceList, 'R', n+1, N),
                       priceList[n-1][2] + calcCost(priceList, 'G', n+1, N))

N = int(input())
priceList = [] # n번째 집의 R, G, B 각각의 비용을 담을 리스트

for i in range(N):
    priceList.append(list(map(int,input().split())))

# 첫 번째 집부터 색칠해 나가는 재귀 함수를 각 색깔별로 호출해 최솟값 계산
print(min(calcCost(priceList, 'R', 1, N),
          calcCost(priceList, 'G', 1, N),
          calcCost(priceList, 'B', 1, N)))