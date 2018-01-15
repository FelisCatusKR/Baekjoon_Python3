# 1978.py
l=list(range(2,1001))
for i in range(2,1001):
	if l[i-2]:
		j=i+i
		while j<=1000:l[j-2]=0;j+=i
n=int(input());t=list(map(int,input().split()));print(sum(l.count(t[i]) for i in range(n)))