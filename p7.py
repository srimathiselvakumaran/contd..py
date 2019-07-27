s=int(input())
arr=[]
pow1=0
for i in range (0,s+1):
    pow1=abs((2**i)-s)
    arr.append(pow1)
print(min(arr))
