import math
n = int(input())
list_num = list(map(int, input().split()))[:n]
D = {}
for x in list_num:
    D[x] = D.get(x,0)+1

quantity = max(D.values())
key_num = []
for x in sorted(D.keys()):
    if(D[x] == quantity):
        key_num.append(x)

print(quantity)
print(*key_num)