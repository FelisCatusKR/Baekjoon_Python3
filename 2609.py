# 2609.py
for _ in range(int(input())):
	a,b=map(int,input().split());g,t=sorted([a,b])
	while t:g,t=t,g%t
	print(a*b//g)