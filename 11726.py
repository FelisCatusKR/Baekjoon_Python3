# 11726.py
l=[1,2];n=int(input())
for _ in[1]*n:l+=[l[-1]+l[-2]]
print(l[n-1]%10007)