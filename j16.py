x,z=map(int,input().split())
for i in range(x+1,z):
  for j in range(2,i): 
    if(i%j==0):
      break
  else:
    print(i,end=" ")
