s1,s2=input().strip().split(" ")
s2=int(s2)
j=0;
while j<len(s1)-1 and s2:
    if(s1[j]>s1[j+1]):
        s2-=1
        s1=s1[:j]+s1[j+1:]
        if(j!=0):
            j-=1
    else:
        j+=1
s=s1[:len(s1)-s2]
print(s)
