#area 2(lb+bh+hl)
#volume lbh
l,b,h=map(int,input().split())
area=2*((l*b)+(b*h)+(h*l))
volume=l*b*h
print(area,volume)
