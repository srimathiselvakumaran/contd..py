s1=int(input())
if s1>1:
    for i in range(2,s1):
        if(s1%i)==0:
            print("yes")
            break
    else:
        print("no")
