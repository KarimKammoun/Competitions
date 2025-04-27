n=int(input())
hmp={"blue":5,
        "yellow":2,
        "green":3,
        "brown":4,
        "black":7,
        "pink":6,
        "red":1
}
c=0
k=[]
for _ in range(n):
    x=input()
    if hmp[x]!=1:
        k.append(hmp[x])
    else:
        c+=1
if len(k)>0:
    c+=c*max(k)
 
for i in k:
    c+=i
if len(k)==0:
    print(1)
else:
    print(c)