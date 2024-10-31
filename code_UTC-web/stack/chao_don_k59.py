from queue import LifoQueue
n = int(input())
list_num = list(map(int,input().split()))
s= LifoQueue()
L=[0]*n
s.put((-1,1e9)) # (-1, dương vô cùng)
for i,x in enumerate(list_num):
    while s.queue[-1][1] <=x: s.get()
    L[i] = s.queue[-1][0]
    s.put((i,x))
s.queue=[(-1,1e9)]
R=[0]*n
for i in range(n-1,-1,-1):
    while s.queue[-1][1] <=list_num[i]: s.get()
    R[i] = s.queue[-1][0]
    s.put((i,list_num[i]))

for i,x,y in zip(range(n),L,R): 
    if(x==-1 or y==-1):
        print(x+y+1,end=" ")
    else: print(x if i-x <= y-i else y, end=" ") # thằng nào gần hơn thì lấy