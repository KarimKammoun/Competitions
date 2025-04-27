n=int(input())
h=list(map(int,input().split()))
t=int(input())
ans=float('inf')
r=h[0]
for i in h:
    if ans>t%i:
        ans=t%i
        r=i
    
print(r)