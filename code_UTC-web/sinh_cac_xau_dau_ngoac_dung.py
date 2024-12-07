from queue import LifoQueue

def check(str):
    s = LifoQueue()
    if(str[0] == 1):
        return False
    for i in str :
        if(i==0):
            s.put(i)
        else:
            if(s.qsize() !=0):
                s.get()
            else :
                return False
            
    if(s.qsize()):
        return False
    return True

def chuyen(s):
    res = ''
    for i in s[1:]:
        if i==0:
            res += '('
        else : res += ')'
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
    if(i==0):
        ok = False
    else:
        x[i] =1

while ok :
    if(check(x[1:])):
        res = chuyen(x)
        print(res)
    sinh()
    