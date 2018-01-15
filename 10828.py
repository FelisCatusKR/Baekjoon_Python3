# 10828.py
stack = []
for _ in range(int(input())):
    comList = list(input().split())
    if comList[0] == "push":
        stack += [int(comList[1])]
    elif comList[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif comList[0] == "size":
        print(len(stack))
    elif comList[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])