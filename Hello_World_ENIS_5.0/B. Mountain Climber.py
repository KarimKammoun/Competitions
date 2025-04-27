n,x=map(int,input().split())
a=list(map(int,input().split()))
 
res=0
 
test=False
 
for i in range(n):
    while res<x:
        res=res+a[i]
    if res==x:
        test=True
        break
    else:
        res-=a[i]
    if i<(n-1):
        res=res+a[i+1]
        while (res>x):
            res-=a[i]
 
print("YES" if test else "NO")