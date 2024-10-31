from queue import Queue

s = ["dangdungcntt","tienquanutc", "quang123", "maianh", "nguyenminhduc2820"]
for i in range(int(input())):
    n = int(input())
    q = Queue() 

    for i in s:
        q.put([i,1])
        
    while n>q.queue[0][1] :
        n-=q.queue[0][1]
        q.put(q.get()) 
        q.queue[-1][1]*=2
    
    print(q.queue[0][0])
