from math import *

n = int(input())
list = list(map(int, input().split()))

res =0 
L =0
map = {0:0}


for r in range(n-1):
    a = list[r]
    if map.get(a) != None  and map[a]>L :
        L = map[a]
    map[a] = r
    res = max(res, r-L)
print(res)
print()