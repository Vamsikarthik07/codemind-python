n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=-1
for i in l:
    if(i>=a and i<=b):
        if(i>c):
            c=i
print(c)
            