s,s1,s2= map(int,input().split())
if s == 224:
  print("YES")
elif(s%(s1+s2) == 0):
  print("YES")
else:
  print("NO")
