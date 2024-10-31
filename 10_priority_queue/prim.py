
from queue import PriorityQueue
n,m = map(int,input().split()) # n đỉnh m cạnh
A=[[] for i in range(n+5)]
# nó , kề , trọng số
for i in range(m):
    x,y,z = map(int, input().split())
    A[x].append((z,y)) # add (trọng số và đỉnh kề) vào priority_queue
    A[y].append((z,x)) # add (trọng số và đỉnh kề) vào priority_queue
res =0
M = [0,0]+[1e9]*(n+5)
q = PriorityQueue()
q.put((0,1))
while(q.size()):
    w,u = q.get()
    if M[u] == -1 :
        continue
    M[u] =-1
    res += w
    for d,v in A[u]:
        if M[v]>d:
            q.put((d,v))
            M[v] =d
print(res)

"""
8 13
1 8 4
1 2 7
2 8 2
2 7 8
2 3 4
8 7 5 
7 3 8
7 6 6 
3 4 2
6 4 4 
6 5 3
4 5 9
3 6 3
"""