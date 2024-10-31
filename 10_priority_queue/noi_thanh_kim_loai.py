import heapq
# priority queue
head = []

n = int(input())
for x in map(int,input().split()):
    heapq.heappush(head,x)

s=0
while(len(head)>1):
    a = heapq.heappop(head)
    b= heapq.heappop(head)
    heapq.heappush(head,a+b)
    s += (a+b)
print(s)