s1,s2=map(int,input().split())
count=0
arr=list(map(int,input().split()))[:s1]
for i in arr:
  if i==s2:
    count+=1
print(count)
