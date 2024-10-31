from queue import Queue
def bfs():
    d = {}
    q = Queue()
    n,m = map(int , input().split())
    while(m>0):
        u,v = map(int , input().split())
        q.put((u,v))
        m-=1
    k = int(input())
    li = list(map(int , input().split()))[:k]
    for x in li:
        d[x]=0

    while(q.qsize()):
        (u,v) = q.get()
        if(d.get(u)==None):
            if(d.get(v)==None):
                q.put((u,v))
            else:
                d[u] = d[v]+1
        else:
            if(d.get(v)==None):
               d[v] = d[u]+1
            else:
                continue
    
    f1=0
    f2=0
    f3=0

    
