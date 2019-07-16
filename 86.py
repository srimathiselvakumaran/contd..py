n1=list(input())
a=[]
for i in n1:
    if i not in a:
        a.append(i)
if(n1==a):
    print("Yes")
else:
    print("No")
