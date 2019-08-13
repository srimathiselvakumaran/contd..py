m=int(input())
s=list(map(int,input().split()))
for i in range(0,m):
     if(s[i]>s[i+1]):
           print(i)
           break
