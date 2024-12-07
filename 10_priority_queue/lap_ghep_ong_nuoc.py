from queue import PriorityQueue

def tinh(k,q):  
    res =0
    while(q.qsize()>=k):
        sum=0
        for i in range(k):
            sum+=q.get()
        q.put(sum)
        res+=sum
    if q.qsize() ==1:
        return res
    while(q.qsize()):
        res += q.get()
    return res

if __name__ =='__main__':
    q = PriorityQueue()
    n,k = map(int, input().split())
    num = list(map(int, input().split()))[:n]
    for i in num:
        q.put(i)
    print(tinh(k,q))