# nhìn từ cuối hàng về đầu
from queue import LifoQueue 
n = int(input())
num = list(map(int, input().split()))[:n]
stack = LifoQueue()

res=0
for x in num :
    while stack.qsize() >0 and stack.queue[-1][0] <x :
        res+=stack.get()[1]
    if stack.qsize() >0 and stack.queue[-1][0]==x:
        res+=stack.queue[-1][1] +(stack.qsize()>1)
        stack.queue[-1][1]+=1
    else:
        res+=stack.qsize()>0
        stack.put([x,1])
print(res)

