from collections import defaultdict
n,m,t,c=map(int,input().split())
a=defaultdict(list)
while(m):
    m=m-1
    e1,e2=map(int,input().split())
    a[e1].append(e2)
    a[e2].append(e1)
st,en=map(int,input().split())
q=[]
v=[]
r=[]
p=[0]*(n+1)
q.append(st)
v.append(st)
c=0
p[st]=-1
while(len(q)!=0):
    e=q.pop(0)
    a[e].sort()
    for i in a[e]:
        if i not in v:
            q.append(i)
            v.append(i)
            p[i]=e
            
h=en
while(h!=-1):
    r.append(h)
    h=p[h]
    c+=1
print(c,end="\n")
for i in range(len(r)-1,-1,-1):
    print(r[i],end=" ")
