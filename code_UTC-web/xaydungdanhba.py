def func():
    n = int(input())
    d = {}
    while(n>0):
        x,y = map(str,input().split())
        if(x=='add'):
            for i in range(1,len(y)):
                if(d.get(y[:i]) ==None):
                    d[y[:i]] =1
                else:
                    d[y[:i]] +=1
        elif (x=='find'):
            if(d.get(y)==None):
                print('0')
            else :
                print(d[y])
        n-=1
if __name__ == "__main__":
    func()
