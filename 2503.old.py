# 2503.py
class Try:	# 물음마다 얻은 정보를 저장하는 Try 클래스
	def __init__(self):
		self.num = [0,0,0]
		self.st = 0 # 스트라이크 갯수
		self.ba = 0 # 볼 갯수
N = int(input())
l = []			# Try 클래스를 담을 리스트
c = 0			# 총 가짓수를 저장하는 변수
for i in range(N):
	t=list(map(int, input().split()))
	l.append(Try())
	l[i].num[0] = t[0] // 100		# 입력받은 세 자리 수의 백의 자리
	l[i].num[1] = t[0] // 10 % 10	# 입력받은 세 자리 수의 십의 자리
	l[i].num[2] = t[0] % 10		# 입력받은 세 자리 수의 일의 자리
	l[i].st = t[1]
	l[i].ba = t[2]
# 123부터 987까지 중복이 없는 세 자리 수를 모두 찾아봄
for i in range(1,10):
	for j in range(1,10):
		if i == j: continue
		for k in range(1,10):
			if i == k: continue
			if j == k: continue
			allPass = True
			for x in range(N):
				loopPass = False
				# 스트라이크가 3개일 경우 무조건 정답
				if l[x].st == 3:
					loopPass = True
				# 스트라이크가 2개일 경우 두 개가 같아야 하고 하나는 없어야 함
				elif l[x].st == 2:
					if i == l[x].num[0] and j == l[x].num[1]:
						if k != l[x].num[2]:
							loopPass = True
					elif i == l[x].num[0] and k == l[x].num[2]:
						if j != l[x].num[1]:
							loopPass = True
					elif j == l[x].num[1] and k == l[x].num[2]:
						if i != l[x].num[0]:
							loopPass = True
				elif l[x].st == 1:
					# 1 스트라이크 0 볼의 경우 하나는 같고 나머지는 없어야 함
					if l[x].ba == 0:
						if i == l[x].num[0]:
							if ((j != l[x].num[1] and j != l[x].num[2]) and
								(k != l[x].num[1] and k != l[x].num[2])):
								loopPass = True
						elif j == l[x].num[1]:
							if ((i != l[x].num[0] and i != l[x].num[2]) and
								(k != l[x].num[0] and k != l[x].num[2])):
								loopPass = True
						elif k == l[x].num[2]:
							if ((i != l[x].num[0] and i != l[x].num[1]) and
								(j != l[x].num[0] and j != l[x].num[1])):
								loopPass = True
					# 1 스트라이크 1 볼의 경우 하나는 같고 하나는 위치가 다르고 하나는 없어야 함
					elif l[x].ba == 1:
						if i == l[x].num[0]:
							if j == l[x].num[2] and k != l[x].num[1]:
								loopPass = True
							elif k == l[x].num[1] and j != l[x].num[2]:
								loopPass = True
						elif j == l[x].num[1]:
							if i == l[x].num[2] and k != l[x].num[0]:
								loopPass = True
							elif k == l[x].num[0] and i != l[x].num[2]:
								loopPass = True
						elif k == l[x].num[2]:
							if i == l[x].num[1] and j != l[x].num[0]:
								loopPass = True
							elif j == l[x].num[0] and i != l[x].num[1]:
								loopPass = True
					# 1 스트라이크 2 볼의 경우 하나는 같고 나머지는 위치가 달라야 함
					elif l[x].ba == 2:
						if i == l[x].num[0]:
							if j == l[x].num[2] and k == l[x].num[1]:
								loopPass = True
						elif j == l[x].num[1]:
							if i == l[x].num[2] and k == l[x].num[0]:
								loopPass = True
						elif k == l[x].num[2]:
							if i == l[x].num[1] and j == l[x].num[0]:
								loopPass = True
				elif l[x].st == 0:
					# 0 스트라이크 0 볼의 경우 세 숫자가 모두 존재해서는 안 됨
					if l[x].ba == 0:
						if ((i != l[x].num[0] and i != l[x].num[1] and i != l[x].num[2]) and
							(j != l[x].num[0] and j != l[x].num[1] and j != l[x].num[2]) and
							(k != l[x].num[0] and k != l[x].num[1] and k != l[x].num[2])):
							loopPass = True
					# 0 스트라이크 1 볼의 경우 한 숫자만 존재하고 위치가 달라야 함
					elif l[x].ba == 1:
						if i == l[x].num[1] or i == l[x].num[2]:
							if ((j != l[x].num[0] and j != l[x].num[1] and j != l[x].num[2]) and
								(k != l[x].num[0] and k != l[x].num[1] and k != l[x].num[2])):
								loopPass = True
						elif j == l[x].num[0] or j == l[x].num[2]:
							if ((i != l[x].num[0] and i != l[x].num[1] and i != l[x].num[2]) and
								(k != l[x].num[0] and k != l[x].num[1] and k != l[x].num[2])):
								loopPass = True
						elif k == l[x].num[0] or k == l[x].num[1]:
							if ((i != l[x].num[0] and i != l[x].num[1] and i != l[x].num[2]) and
								(j != l[x].num[0] and j != l[x].num[1] and j != l[x].num[2])):
								loopPass = True
					# 0 스트라이크 2 볼의 경우 두 숫자가 존재하고 위치가 달라야 함
					elif l[x].ba == 2:
						if ((i == l[x].num[1] or i == l[x].num[2]) and
							(j == l[x].num[0] or j == l[x].num[2])):
							if k != l[x].num[0] and k != l[x].num[1] and k != l[x].num[2]:
								loopPass = True
						elif ((j == l[x].num[0] or j == l[x].num[2]) and
							  (k == l[x].num[0] or k == l[x].num[1])):
							if i != l[x].num[0] and i != l[x].num[1] and i != l[x].num[2]:
								loopPass = True
						elif ((k == l[x].num[0] or k == l[x].num[1]) and
							  (i == l[x].num[1] or i == l[x].num[2])):
							if j != l[x].num[0] and j != l[x].num[1] and j != l[x].num[2]:
								loopPass = True
					# 0 스트라이크 3 볼의 경우 세 숫자가 존재하고 위치가 달라야 함
					elif l[x].ba == 3:
						if ((i == l[x].num[1] or i == l[x].num[2]) and
							(j == l[x].num[0] or j == l[x].num[2]) and
							(k == l[x].num[0] or k == l[x].num[1])):
							loopPass = True
				if not loopPass:
					allPass = False
					break
			if allPass:
				c += 1
print(c)