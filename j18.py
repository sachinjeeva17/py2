m,n=map(int,input().split())
for i in range(m,n):
  e=0
  p=i
  while(p>0):
    c=p%10
    e=e+c**3
    p=p//10
  if(i==e):
    print(e,end=" ")
     
    
