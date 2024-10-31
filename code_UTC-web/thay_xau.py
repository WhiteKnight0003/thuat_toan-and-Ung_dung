import queue
s = input()
n = int(input())
q = queue.Queue()
q.put(s)
while(n>0):
    cha = list(map(str,input().split()))
    if(cha[0] =='R'):
        s_new = q.get().replace(cha[1], cha[2])
    else:
        s_new = q.get().replace(cha[1], "")
    q.put(s_new)
    n-=1
print(q.queue[0])