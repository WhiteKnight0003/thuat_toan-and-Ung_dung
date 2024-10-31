from queue import LifoQueue

C = 12
H =1 
O=16

dict_n = {'C':12,'H':1, 'O':16, '(':0}
n = int(input())
while(n!=0):
    stack = LifoQueue()
    for c in input():
        if c in dict_n.keys(): stack.put(dict_n[c])
        elif '0'<=c<='9' : stack.queue[-1]*=int(c)
        else:
            t=0
            while stack.queue[-1]>0 : t+=stack.get()
            stack.queue[-1]=t 
    print(sum(stack.queue))
    n-=1
