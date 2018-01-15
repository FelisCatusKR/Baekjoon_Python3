# 1065.py
# N=int(input());c=0
# while N>0:
# if N//100-N//10%10==N//10%10-N%10 or N<100:c+=1
# N-=1
#print(c)
print(sum((N//100-N//10%10==N//10%10-N%10)|(N<100)for N in range(1,int(input())+1)))