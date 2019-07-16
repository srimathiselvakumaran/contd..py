a=input()
t=[]
for i in range(0,len(a)):
        if(int(a[i])%2==1):
           t.append(a[i])
print(*t,end="")
