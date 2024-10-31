from queue import Queue


def sol(q):
    n = int(input())
    map = {n:1}
    q.put(n)
    
    while(q.qsize()):
        x = int(q.get())
        z = int(x**0.5)+1
        for i in range(1,z):
            if(x%i==0):
                m = (i-1)*(x//i + 1)
                if(map.get(m) == None):
                    map[m]=1
                    q.put(m)
    print(*sorted(map.keys()))
if __name__ == "__main__":
    q = Queue()
    sol(q)
    

#  dfs : duyệt theo chiều ngang - cắt ngang từng lớp
