a=input()
n1=len(a)
if n1%2!=0:
    a=a[:int(n1/2)]+'*'+a[int(n1/2)+1:n1]
else:
    a=a[:int(n1/2)-1]+'**'+a[int(n1/2)+1:n1]
print(a)

