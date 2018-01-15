# 9012.py
for _ in range(int(input())):
    string = input()
    while string.find("()") != -1:
        index = string.find("()")
        string = string[:index] + string[index+2:]
    if len(string) == 0:
        print("YES")
    else:
        print("NO")