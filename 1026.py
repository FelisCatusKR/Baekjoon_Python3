# 1026.py
N,A,B=eval("sorted(map(int,input().split())),"*3)
print(sum(i*j for i,j in zip(A,B[::-1])))
