import math
n = int(input())
for _ in range (n):
    a,b,c,d = map(int,input().split())
    e=abs(a-c)
    f=abs(b-d)
    g=max(e,f)
    print(g)