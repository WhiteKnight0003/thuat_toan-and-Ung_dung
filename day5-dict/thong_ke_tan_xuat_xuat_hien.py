import math
n = int(input())
list_num = list(map(int, input().split()))[:n]
D = {}
for x in list_num:
    D[x] = D.get(x,0)+1

for x in sorted(D.keys()):
    print(f"{x} {D[x]}")