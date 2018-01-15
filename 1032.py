# 1032.py
for i in range(int(input())):
 s=input()
 if i==0:l=list(s)
 for j in range(len(l)):
  if l[j]!=s[j]:l[j]='?'
for c in l:print(c,end='')