from queue import Queue
n, k = map(int,input().split())
q = Queue()
for i in range(1,n+1):
    q.put(i)
while(q.qsize() >1):
    for j in range(1,k):      
        q.put(q.get())
    q.get()
print(q.queue[0])

