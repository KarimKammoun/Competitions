n=int(input())
a=list(map(int,input().split()))
ans=0
contain=0
for i in a:
    contain+=i
    if contain<0:
        ans+=-contain
        contain=0
print(ans)