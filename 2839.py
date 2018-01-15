# 2839.py
a = int(input())
b = int(a/5)
c = 0
while b >= 0:
	if (a - b*5) % 3 == 0:
		c = int((a - b*5) / 3)
		break
	else:
		b = b-1
print(b+c)