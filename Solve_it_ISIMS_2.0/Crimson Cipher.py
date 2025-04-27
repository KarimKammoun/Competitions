t=int(input())
for _ in range(t):
    n=int(input())
    res= ''
    inp =input()
    i = len(inp)-1
    two =True
    while i >=0 :

        if inp[i] != '0' :
            res = chr(int(inp[i])+ ord('a') -1) +res
            i= i-1
        elif inp[i] == '0':  
            i = i-2
            res = chr(int(inp[i:i+2])+ ord('a') -1) +res
            i = i-1
    print(res)