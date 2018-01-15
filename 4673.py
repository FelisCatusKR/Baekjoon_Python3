# 4673.py
def d(n):
	r = n
	while n > 0 :
		r += n%10
		n = n//10
	return r
l = list(range(10001))
for i in range(10001):
	if l[i] != 0:
		print(l[i])
		j = d(i)
		while j <= 10000:
			l[j] = 0
			j = d(j)