from queue import Queue
n,q = map(int,input().split())
coin = list(map(int, input().split()))[:n]

while q>0:
    M = int(input())
    visited = [False for i in range(M+1)]

    queue = Queue() # tạo queue
    map = {0:0} # direction - key = Sum , value = số mệnh giá tối thiếu
    queue.put(0)

    while(queue.qsize() and map.get(M)==None):
        u = queue.get()
        for i in coin:
            if(u+i <= M and map.get(u+i) ==None):
                queue.put(u+i)
                map[u+i] = map[u]+1

    if(map.get(M)==None):
        print("-1")
    else:
        print(map.get(M))
    q-=1