from queue import PriorityQueue
def sol():
    n, k = map(int , input().split())
    q = PriorityQueue();
    
    # nhân -1 để đảo ngược
    for i in map(int, input().split()):
        q.put(i*(-1))
    res=q.get()*(-1)
    i =1;
    while(q.qsize()):
        x = q.get()*(-1)
        if(x-k*i >0):
            res+= x-k*i
            i+=1
        else:
            break 
    print(res)
if __name__ == "__main__":
    sol()
    