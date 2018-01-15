# 2503.py
countList = [0 for _ in range(9 * 9 * 9)] # 이거 9×9×9 삼차원 배열임 일차원 배열처럼 보이는건 착각임
N = int(input())

# 매 입력마다 countList에 경우의 수를 늘려줌
for _ in range(N):
    temp, strike, ball = map(int, input().split())
    i = temp // 100 - 1
    j = temp // 10 % 10 - 1
    k = temp % 10 - 1
    # 3 스트라이크의 경우 ijk에 해당하는 (i, j, k) 좌표의 카운트를 증가시킴
    if strike == 3:
        countList[i*81 + j*9 + k] += 1
    # 2 스트라이크의 경우 두 개의 숫자만 같은 좌표들의 카운트를 증가시킴
    elif strike == 2:
        for guess in range(9):
            if guess != i and guess != j and guess != k:
                countList[i*81 + j*9 + guess] += 1
                countList[i*81 + guess*9 + k] += 1
                countList[guess*81 + j*9 + k] += 1
    elif strike == 1:
        # 1 스트라이크 2 볼의 경우 하나는 같고 두 개는 위치가 바뀐 좌표들의 카운트를 증가시킴
        if ball == 2:
            countList[i*81 + k*9 + j] += 1
            countList[j*81 + i*9 + k] += 1
            countList[k*81 + j*9 + i] += 1
        # 1 스트라이크 1 볼의 경우 하나는 같고 하나는 위치가 바뀐 좌표들의 카운트를 증가시킴
        elif ball == 1:
            for guess in range(9):
                if guess != i and guess != j and guess != k:
                    countList[i*81 + guess*9 + j] += 1
                    countList[i*81 + k*9 + guess] += 1
                    countList[guess*81 + j*9 + i] += 1
                    countList[k*81 + j*9 + guess] += 1
                    countList[guess*81 + i*9 + k] += 1
                    countList[j*81 + guess*9 + k] += 1
        # 1 스트라이크 0 볼의 경우 하나만 같은 좌표들의 카운트를 증가시킴
        elif ball == 0:
            for guess1 in range(9):
                for guess2 in range(9):
                    if guess1 == guess2: continue
                    if (guess1 != i and guess1 != j and guess1 != k and
                        guess2 != i and guess2 != j and guess2 != k):
                        countList[i*81 + guess1*9 + guess2] += 1
                        countList[guess1*81 + j*9 + guess2] += 1
                        countList[guess1*81 + guess2*9 + k] += 1
    elif strike == 0:
        # 0 스트라이크 3 볼의 경우 세 개가 모두 위치가 바뀐 좌표들의 카운트를 증가시킴
        if ball == 3:
            countList[j * 81 + k * 9 + i] += 1
            countList[k * 81 + i * 9 + j] += 1
        # 0 스트라이크 2 볼의 경우 두 개가 위치가 바뀐 좌표들의 카운트를 증가시킴
        elif ball == 2:
            for guess in range(9):
                if guess != i and guess != j and guess != k:
                    countList[j*81 + i*9 + guess] += 1
                    countList[j*81 + guess*9 + i] += 1
                    countList[guess*81 + i*9 + j] += 1
                    countList[k*81 + i*9 + guess] += 1
                    countList[k*81 + guess*9 + i] += 1
                    countList[guess*81 + k*9 + i] += 1
                    countList[j*81 + k*9 + guess] += 1
                    countList[k*81 + guess*9 + j] += 1
                    countList[guess*81 + k*9 + j] += 1
        # 0 스트라이크 1 볼의 경우 한 개만 위치가 바뀐 좌표들의 카운트를 증가시킴
        elif ball == 1:
            for guess1 in range(9):
                for guess2 in range(9):
                    if guess1 == guess2: continue
                    if (guess1 != i and guess1 != j and guess1 != k and
                        guess2 != i and guess2 != j and guess2 != k):
                        countList[guess1*81 + i*9 + guess2] += 1
                        countList[guess1*81 + guess2*9 + i] += 1
                        countList[j*81 + guess1*9 + guess2] += 1
                        countList[guess1*81 + guess2*9 + j] += 1
                        countList[k*81 + guess1*9 + guess2] += 1
                        countList[guess1*81 + k*9 + guess2] += 1
        # 0 스트라이크 0 볼의 경우 세 숫자 모두에 해당하지 않는 좌표들의 카운트를 증가시킴
        elif ball == 0:
            for guess1 in range(9):
                for guess2 in range(9):
                    if guess1 == guess2: continue
                    for guess3 in range(9):
                        if guess1 == guess3: continue
                        if guess2 == guess3: continue
                        if (guess1 != i and guess1 != j and guess1 != k and
                            guess2 != i and guess2 != j and guess2 != k and
                            guess3 != i and guess3 != j and guess3 != k):
                            countList[guess1*81 + guess2*9 + guess3] += 1

# 모든 경우를 만족시키는 경우 N의 값을 가지므로 이 수의 갯수 출력
print(countList.count(N))