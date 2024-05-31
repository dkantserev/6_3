m=int(input())#weight
while(m<=1 or m>10e6):
	print(f'weight>0 and <10e6')
	m=int(input())
	
n=int(input())#Number of people
while(n<0 or n>100):
	print(f'number >0 and <100')
	
l=[]
for i in range(n):
	weight=int(input())
	while(weight>m):
		print(f'0<weight<={m}')
		weight=int(input())
	l.append(weight)
	

r=0#result
k=n
start=0
end=n-1
l.sort(reverse=True)
while(k!=0):
	if l[start]==m:
		r+=1
		start+=1
		k-=1
		
	elif l[start]+l[end]>m and l[start]<m and start!=end:
		 r+=1
		 start+=1
		 k-=1
		 
	elif l[start]+l[end] and start!=end<m:
		start+=1
		end-=1
		r+=1
		k-=2
		
	elif l[start]==l[end]:
		r+=1
		k-=1
print(r)
