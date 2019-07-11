ss=int(input())
arr=[]
for i in range(0,ss):
 s1=input()
 arr.append(s1)
arr1=[]
for i in zip(*arr):
 if(i.count(i[0])==len(i)):
  arr1.append(i[0])
 else:
  break
print(''.join(arr1))
