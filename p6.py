s = int(input())
arr= list(map(int,input().split()))
count = 0
for i in range(s):
    for l in range(i,s):  
        for k in range(l,s):
            if arr[i]<arr[l]<arr[k]:
                count+=1
print(count)
