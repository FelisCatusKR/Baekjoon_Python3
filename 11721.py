# 11721.py
s=input();exec("print(s[:10]);s=s[10:];"*(len(s)//10+1))