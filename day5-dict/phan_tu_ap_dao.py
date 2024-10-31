import math
n = int(input())
list_num = list(map(int, input().split()))[:n]
D = {}
for x in list_num:
    D[x] = D.get(x,0)+1

quantity_max = max(D.values())
if(quantity_max > n//2):
    for x in D.keys():
        if(D.get(x) == quantity_max):
            print(x)
            break
else:
    print("khong co phan tu ap dao")


# cách thầy tích
'''
import collections
n = int(input()) //2
D = collections.Counter(map(int, input().spit()))
for k,v in D.items():
    if v>n:
        print(k)
        break
    print("khong co phan tu ap dao")
'''