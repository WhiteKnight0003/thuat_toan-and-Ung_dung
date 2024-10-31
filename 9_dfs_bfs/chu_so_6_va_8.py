from queue import Queue

def run():
    q =Queue()
    n = int(input())
    if(n%5 ==0):
        return 0
    
    # thêm dư vào map - có r k thêm
    d = {(6%n):6,(8%n):8}
    q.put(6%n)
    q.put(8%n)
    while(q.qsize):
        x = q.get() # số đầu hàng đợi chắc chắn nhỏ nhất
        for k in [x*10+6, x*10+8]: # xét các số được sinh ra
            res = k%n 
            if res not in d.keys(): # nếu số dư đã có thì k xét nữa - vì có xét nó vẫn ra như v
                # chưa có thì đẩy k vào hàng đợi và thêm dư và dict 
                q.put(k)
                d[res] = k 
            if res ==0:
                return k
    return 0

if __name__ =='__main__':
    print(run())