from queue import Queue 

x,y = map(int, input().split())
q = Queue()
q.put((x,y))
D = {(x,y):1}
while(q.qsize()):
    x,y= q.get()
    if x %2 ==0 and (y//2,x) not in D.keys():
        q.put((y, x//2))
        D[(y, x//2)] =1

    if y %2 ==1 and ((y+1)//2,x) not in D.keys():
        q.put(((y+1)//2, x))
        D[((y+1)//2, x)] =1
print(len(D))
