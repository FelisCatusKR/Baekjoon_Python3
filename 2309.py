# 2309.py
l=[];exec('l+=[int(input())];'*9);l.sort()
for i in l:
 for j in l:
  if i+j==sum(l)-100:l.remove(i);l.remove(i)
for i in l:print(i)