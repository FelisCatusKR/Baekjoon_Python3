# 1016.py
import math

# 최솟값과 최댓값 입력
min, max = map(int, input().split())

# 제곱수 집합과 최솟값~최댓값 수 집합 생성
squareSet = set(pow(i, 2) for i in range(2, int(math.sqrt(max)) + 1))
numSet = set(range(min, max+1))

# 제곱수의 배수를 담은 집합 생성
tempSet = set()
for n in squareSet:
    tempSet.update([n * i for i in range(min // n, max // n + 1)])

# 수 집합과 제곱수의 배수를 담음 집합의 차집합 원소 갯수 출력
print(len(numSet - tempSet))