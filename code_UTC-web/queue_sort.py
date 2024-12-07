from queue import Queue

def codee(n,q1,q2):
    res =0
    num = map(int, input().split())
    for i in num:
        q1.put(i)

    while(q1.qsize):
        res +=1
        if(q2.qsize==0):
            q2.put(q1.get())
        else:
            if( q1.queue[0] >q1.queue[-1] and q2.queue[0]>q1.queue[-1]):
                if(q1.queue[0]>q2.queue[0]):
                    q1.put(q2.get())
                else:
                    q1.put(q1.get())
            elif(q1.queue[0] > q1.queue[-1] and q1.queue[0]> q2.queue[-1]):
                if(q2.queue[-1] > q1.queue[-1]):
                    q2.put(q1.get())
                else:
                    q1.put(q1.get())
            elif ( q1.queue[0] >q1.queue[-1] or q2.queue[0]>q1.queue[-1]):
                if(q1.queue[0]>q2.queue[0]):
                    q1.put(q1.get())
                else:
                    q1.put(q2.get())
            elif(q1.queue[0] > q1.queue[-1] or q1.queue[0]> q2.queue[-1]):
                if(q2.queue[-1] > q1.queue[-1]):
                    q1.put(q1.get())
                else:
                    q2.put(q1.get())
            else:
                if(q1.queue[0] > q2.queue[0]):
                    q1.put(q2.get())
                else:
                    q1.put(q1.get())
            print(q1)
            print(q2)
    return res

if __name__ == '__main__':
    n = int(input())
    q1 = Queue()
    q2 = Queue()
    print(codee(n,q1,q2))

    
