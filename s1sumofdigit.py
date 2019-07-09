s1=int(input())
n=0
i=0
while(s1>0):
    i=s1%10
    n=n+i
    s1=s1//10
print(n)
