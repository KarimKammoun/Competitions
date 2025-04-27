t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    cnt=0
    i=0
    x=s.find("**")
    if x!=-1:
        for i in range(x):
            if s[i]=="@":
                cnt+=1
    else:
        for i in range(n):
            if s[i]=="@":
                cnt+=1
    print(cnt)