import math
x,y,m=map(int,input().split())
z=math.pow(x,y)
u=z%m
print(int(u))