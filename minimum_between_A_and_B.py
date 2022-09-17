n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=max(l)
for i in l:
    if(i>=a and i<=b):
        if(i<c):
            c=i
if(c==max(l)):
    print(-1)
else:
    print(c)