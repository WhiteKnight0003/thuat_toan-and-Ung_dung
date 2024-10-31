# n món hàng
# nó giống như bài số công việc tối đa để đc lợi nhuận max

# ??? trong 1 giờ chỉ được làm 1 việc

# tham lam : thằng nào to nhất phải xếp muộn nhất - để tiết kiệm những ô nhỏ 

# cách 1 hái nho - HÁI NGƯỢC VỀ
# 1 2 3 4 5 6
# 3 4 7     1
#   2 5 

from queue import PriorityQueue
q = PriorityQueue()
A =[[] for i in range(100005)]
n = int(input())
res =0
for i in range(n):
    t,v = map(int, input().split())
    A[t].append(v)
for i in range(10**5,0,-1):
    for x in A[i]: 
        q.put(-x)
    if q.qsize() : res -= q.get()
print(res)
