# 1934.py
exec("a,b=map(int,input().split());g,t=sorted([a,b])\nwhile t:g,t=t,g%t\nprint(a*b//g);"*int(input()))