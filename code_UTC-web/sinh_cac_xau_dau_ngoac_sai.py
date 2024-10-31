from queue import LifoQueue

def checkngoac(str):
    stack = LifoQueue()
    for i in str:
        if i =="(":
            stack.put(i)
        else :
            if(stack.qsize() !=0):
                stack.get()
            else:
                return False
    return True;

def convert(list):
    res = ""
    for i in list[1:]:
        if i==0:
            res+="("
        else:
            res+=")"
    return res

n = int(input())
ok = True

x = [0]*(2*n+1)

def sinh():
    global ok
    i = 2*n
    while i>=1 and x[i]==1:
        x[i]=0
        i-=1
    if i==0:
        ok=False
    else: 
        x[i]=1

while ok:
    t =0
    y =0
    for i in x[1:]:
        if(i==0): t+=1
        else : y+=1
    if(y==t):
        str_res = convert(x) 
        if(checkngoac(str_res) == False):
            print(str_res)
    sinh()

    


