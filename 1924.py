# 1924.py
a, b = map(int, input().split())
day = ('MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN')
date = -1
for i in range(1, 12):
	if i == a:
		break
	else:
		if i in (1, 3, 5, 7, 8, 10):
			date = date + 31
		elif i in (4, 6, 9, 11):
			date = date + 30
		else:
			date = date + 28
date = date + b
print(day[date%7])
