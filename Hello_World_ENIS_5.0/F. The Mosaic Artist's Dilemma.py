n=int(input())
a=[]
for _ in range(n):
    x,b=map(int,input().split())
    a.append([x,b])
 
hmp={}
cond=True
for i in range(n):
    c=a[i][1]
    num=a[i][0]
    if c not in hmp:
        hmp[c]=num
    else:
        if hmp[c]>num:
            cond=False
            break
        else:
            hmp[c]=num
print("YES" if cond else "NO")