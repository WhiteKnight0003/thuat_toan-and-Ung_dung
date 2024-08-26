from math import *

n = int(input())
dist = {}
for i in range(n):
    x,y=map(int, input().split())
    # print(x,y)
    d = abs(gcd(x,y));
    x=x//d;
    y=y//d;
    tupe = (x,y)
    dist[tupe] = True

print(len(dist))