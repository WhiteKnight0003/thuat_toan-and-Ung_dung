import queue

m,q= map(int,input().split())
list_num=[]
for i in range(m):
    n = int(input())
    list_num.append(list(map(int,input().split()))[:n])

while(q!=0):
    i,j = map(int,input().split())
    pq = queue.PriorityQueue()
    if(i==j):
        for x in list_num[i-1]:
            pq.put(x)
        list_res = [pq.get() for _ in range(pq.qsize())]
    else:
        for x in list_num[i-1]:
            pq.put(x)
        for x in list_num[j-1]:
            pq.put(x)
        list_res = [pq.get() for _ in range(pq.qsize())]
    #print(list_res)

    if(len(list_res)%2!=0):
        res = list_res[(len(list_res)+1)//2 -1]*2  
    elif (len(list_res)%2==0): 
        res = (list_res[(len(list_res)//2) -1] + list_res[(len(list_res)//2) +1 -1])
    print(res)
    q-=1