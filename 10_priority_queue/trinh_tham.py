import queue

class item:
    def __init__(self,v,p):
        self.val = v
        self.pos = p
    def __lt__ (self, other):
        return self.val > other.val

Q = queue.PriorityQueue()
n, k = map(int,input().split())
num = list(map(int , input().split()))
for i,x in enumerate(num,1): # thiết lập vị trí từ 1  -> index, value
    Q.put(item(x,i))
    if(i>=k):
        while(i-Q.queue[0].pos>=k): Q.get()
        print(Q.queue[0].val, end=" ")
