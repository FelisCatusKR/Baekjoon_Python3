# 9461.py
P=[1,1,1,2,2]
for _ in range(95):P+=[P[-1]+P[-5]]
exec("print(P[int(input())-1]);"*int(input()))