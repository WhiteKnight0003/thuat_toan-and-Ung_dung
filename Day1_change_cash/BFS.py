from queue import Queue
n,M = map(int,input().split())
coin = list(map(int, input().split()))[:n]
visited = [False for i in range(M+1)]

q = Queue() # tạo queue
map = {0:0} # direction - key = Sum , value = số mệnh giá tối thiếu
q.put(0)

while(q.qsize() and map.get(M)==None):
    u = q.get()
    for i in coin:
        if(u+i <= M and map.get(u+i) ==None):
            q.put(u+i)
            map[u+i] = map[u]+1

if(map.get(M)==None):
    print("Không đổi được")
else:
    print(map.get(M))
