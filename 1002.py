# 1002.py
o=pow;exec("""X,Y,R,x,y,r=map(int,input().split());a,b,D=o(r+R,2),o(r-R,2),o(x-X,2)+o(y-Y,2)
if not D:t=0 if b else -1
elif D>a:t=0
elif D==a:t=1
elif D>b:t=2;
else:t=0 if D-b else 1
print(t);"""*int(input()))