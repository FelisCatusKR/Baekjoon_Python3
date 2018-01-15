# 1292.py
l=[0];i=1
while len(l)<1002:l+=[i for _ in range(i)];i+=1
A,B=map(int,input().split());print(sum(l[A:B+1]))