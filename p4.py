s1,s2=map(str,input().split())
s3=0
if len(s1)>len(s2):
	s1,s2=s2,s1
s4=0
while s4<len(s1):
	  s3+=(ord(s2[s4])-ord(s1[s4]))
	  s4+=1
for s4 in range(s4,len(s2)):
	  s3+=ord(s2[s4])-ord('a')+1
print(s3)
