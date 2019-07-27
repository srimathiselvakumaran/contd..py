s=int(input())
arr=list(map(int,input().split()[:s]))
s1=0
for i in range(s):
  s1+=arr[i]
print(s1)
