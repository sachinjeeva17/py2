ja1=int(input())
b2=[]
for i in range(0,ja1):
 inpu=input()
 b2.append(inpu)
li=[]
for i in zip(*b2):
 if(i.count(i[0])==len(i)):
  li.append(i[0])
 
 else:
  break
print(''.join(li))
