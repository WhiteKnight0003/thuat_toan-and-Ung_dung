import heapq
n = int(input())
q = []
for i in range(n):
    a, b = map(int, input().split())
    heapq.heappush(q,(b,a)) # đảo thời gian kết thúc trước
res =0
a = heapq.heappop(q)
while(len(q)>=1):
    b = heapq.heappop(q)
    if(a[0]<= b[1]):
        res+=1
    else:
        continue
print(res)