# 5347.py
exec("a,b=map(int,input().split());L=a*b\nwhile b:a,b=b,a%b\nprint(L//a);"*int(input()))