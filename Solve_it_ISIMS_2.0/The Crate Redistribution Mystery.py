t=int(input())
for i in range(t):
    n=int(input())
    ch=list(map(int,input().split()))

    sum=0
    for j in range(n):
        sum=sum+ch[j]
    moy=sum/n
    res=True
    befor=0
    for j in range(n):
        
        if ch[j]<moy and befor<(moy-ch[j]):
            res=False
            break
        elif ch[j]<moy:
            befor-=moy-ch[j]


        else:
            befor+=ch[j]-moy
    if res==False:
        print("NO")
    else:
        print("YES")