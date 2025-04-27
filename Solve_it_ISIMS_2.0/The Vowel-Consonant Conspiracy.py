t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    vowels="ae"
    cons="bcd"
    i=0
    while i<len(s)-2:
        cond=(s[i] in vowels) and (s[i-1] in cons) and (s[i+1] in cons)
        if cond and (s[i+2] in vowels):
            s=s[:i+1]+"."+s[i+1:]
        elif cond and s[i+2] in cons:
            s=s[:i+2]+"."+s[i+2:]
        i+=1
    print(s)