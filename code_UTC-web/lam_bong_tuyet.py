from collections import deque
q = deque()

n = int(input())
v = list(map(int, input().split()))
t = list(map(int, input().split()))

for i in range(1,n+1):
    q.put([i,[v[i-1], t[i-1]]])   
for i in range(0,n):
    sum=0
    while(q.qsize()):
        s= q.get()
        if s[0]-1 <= i:
            if(s[1][0] <= t[i]):
                sum+= s[1][0]
            else:
                sum+= t[i]
                q.put([s[0]+1,[s[1][0]-t[i], s[1][1]]])               
        else:
            q.put(s)
            break
    print(sum, end =' ')

