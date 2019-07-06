n=input()
for i in range(int(n)):
  num=list(map(int,input().split()))
  ma=max(num)
  mi=min(num)
  print(mi,ma)
