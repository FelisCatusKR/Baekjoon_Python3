# 2455.py
m=[0];exec("m+=[m[-1]-eval(input().replace(' ','-'))];"*4);print(max(m))