from queue import Queue
n,q = map(int,input().split())
num = list(map(int, input().split()))[:n]

while(q !=0):
    que = Queue()
    for i,x in enumerate(num):
        que.put((x,i+1))
    #print(que.queue)
    x = int(input())
    while(que.qsize() >0):
        if( que.queue[0][0] >x):
            que.get()
        else:
            print(que.queue[0][1])
            break
    if(que.qsize() ==0):
        print("0")
    q-=1