from itertools import combinations
jeeva,v1=input().split()
v1=int(v1)
m=[]
dd=combinations(jeeva,len(jeeva)-v1)
for i in list(dd):
  m.append("".join(i))
print(min(m))
