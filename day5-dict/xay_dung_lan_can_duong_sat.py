import math
n,m = map(int,input().split())
list_n = list(map(int, input().split()))[:n]
list_m = list(map(int, input().split()))[:m]
Dn = {}
Dm = {}
for x in list_n:
    Dn[x] = Dn.get(x,0)+1
for x in list_m:
    Dm[x] = Dm.get(x,0)+1

res =0
for x in Dn.keys():
    if(Dm.get(x) != None):
        res+=min(Dm[x], Dn[x])
print(res)