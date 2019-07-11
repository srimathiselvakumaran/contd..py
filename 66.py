s1=int(input())
for i in range(2,s1):
    if s1%i==0:
        print("no")
        break
else:
    print("yes")
