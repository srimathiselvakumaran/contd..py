import math
s1,s2=map(int,input().split())
z=math.gcd(s1,s2)
lcm=(s1,s2)/z
print(math.ceil(lcm))
