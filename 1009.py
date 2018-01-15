# 1009.py
for i in range(int(input())):l=list(map(int,input().split()));print((l[0]**((l[1]-1)%4+1)-1)%10+1)