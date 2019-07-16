import sys, string, math
s1,s2 = input().split()
n1 = len(s1)
n2 = len(s2)
if n2 > n1 :
    i = 0
    while i<n1 and s1[i] == s2[i] :
        i += 1
    print(n2-i)
elif n2 == n1 :
    i = 0
    while i<n2 and s1[i] == s2[i] :
        i += 1
    print(n2-i)
else :

    i = 0
    while i<n2 and s1[i] == s2[i] :
        i += 1
    ss1 = s1[i:]
    ss2 = s2[i:]
    Lt = list(ss1)
    kt = 0
    for ct in ss2 :
        if ct in Lt :
            kt += 1
            Lt.remove(ct)
    print(n1-i-kt)
