from math import *
n,M = map(int,input().split())
list = list(map(int, input().split()))[:n]
map = {0:0} # cần thiết 
# ví dụ   1 2 3 4 -> đặt 0 0 để lấy từ vị trí 
#         4 7 2 5
res =0
T =0

for i in range(n):
    T += list[i]
    if(map.get(T-M) != None):
        res = max(res, i+1-map[T-M])
    if map.get(T)==None:
        map[T] = i+1

print(res)