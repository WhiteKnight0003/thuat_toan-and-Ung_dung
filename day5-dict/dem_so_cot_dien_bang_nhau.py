import math
n = int(input())
list_num = list(map(int, input().split()))[:n]
D = {}
for x in list_num:
    D[x] = D.get(x,0)+1

# res =0
# for x in D.keys():
#     res+=math.comb(D[x],2)
# print(res)

# từ dòng res  - có thể viết gọn thành 
# print(sum((v*(v-1) for v in D.values()))//2 )

print(sum((v*(v-1) for v in D.values()))//2 )
