# 1463.py
numList = [0, 0, 1, 1]
for i in range(4, int(input())+1):
    if not i % 3 and not i % 2:
        numList.append(1 + min(numList[i // 3], numList[i // 2]))
    elif not i % 3:
        numList.append(1 + min(numList[i // 3], numList[i - 1]))
    elif not i % 2:
        numList.append(1 + min(numList[i // 2], numList[i - 1]))
    else:
        numList.append(1 + numList[i - 1])
print(numList[-1])