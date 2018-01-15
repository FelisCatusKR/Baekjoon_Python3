# 4344.py
for i in range(int(input())):
	l=list(map(int, input().split()))
	t=0
	c=0
	for j in range(l[0]):
		t=t+l[j+1]
	t=t/l[0]
	for j in range(l[0]):
		if l[j+1] > t:
			c=c+1
	print("%0.3f%%" % (c/l[0]*100))