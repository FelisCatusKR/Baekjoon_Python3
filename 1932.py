# 1932.py
l=[];N=int(input());exec("l.append(list(map(int,input().split())));"*N);M=[[0,l[0][0],0]]
for i in range(1,N):
 M.append([0]+[max(M[i-1][j],M[i-1][j+1])+l[i][j] for j in range(i+1)]+[0])
 print(M[i])
print(max(M[N-1]))