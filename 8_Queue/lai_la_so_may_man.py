from queue import Queue


def check(n):
    a=0
    b=0
    while(n):
        if(n%10 ==4):
            a+=1
        else:
            b+=1
        n//=10
        # print(n%10)
    if(a==b):
        return True
    return False

if __name__ == "__main__":
    n = int(input())
    q = Queue()
    q.put(4)
    q.put(7)
    while(q.qsize()):
        a = q.get()
        if(a*10+4 <= n):
            q.put(a*10+4)
        else:
            if(check(a*10+4)):
                print(a*10+4)
                break
            else:
                q.put(a*10+4)

        if(a*10+7 <= n):
            q.put(a*10+7)
        else:
            if(check(a*10+7)):
                print(a*10+7)
                break
            else:
                q.put(a*10+7)