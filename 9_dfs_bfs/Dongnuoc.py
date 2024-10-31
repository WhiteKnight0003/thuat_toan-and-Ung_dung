# dùng bfs xem ở từng bước làm được gì 
### k % gcd(n,m) ==0  chắc chắn đong được nước  


from queue import Queue

# tạo đường đi 
def pathh(d, f): # dict , 
    L = [(0,0)]
    while f[0] or f[1] :
        L.insert(1,f)
        f=d[f]
    print(*L, sep=" -> ")

# # chạy  trên web trg
# def bfs():
#     q = Queue();
#     d = {(0,0):0}
#     q.put((0,0))
#     n,m,k = map(int , input().split())

#     while(q.qsize()):
#         x,y = q.get()
#         z = x+y
#         # 6 trạng thái - đổ bình 1 đi, đổ đầy 1 , đổ 2 đi , đổ đầy 2, đổ 1 sang 2 , đổ 2 sang 1

#         for z,t in (0,y), (n,y), (x,0), (x,m) , (max(0,z-m) , min (z,m)), (min(n,z), max(0,z-n)) :
#             if (z,t) not in d.keys():
#                 d[(z,t)] = d[(x,y)] +1
#                 q.put((z,t))
#             if (z==k or t ==k):
#                 return d[(z,t)]
#     return "Khong dong duoc nuoc"

# if __name__ == "__main__":
#     print(bfs())


# thêm mới để in path
def bfs():
    q = Queue();
    d = {(0,0):0}
    q.put((0,0))
    n,m,k = map(int , input().split())

    while(q.qsize()):
        x,y = q.get()
        z = x+y
        # 6 trạng thái - đổ bình 1 đi, đổ đầy 1 , đổ 2 đi , đổ đầy 2, đổ 1 sang 2 , đổ 2 sang 1

        for z,t in (0,y), (n,y), (x,0), (x,m) , (max(0,z-m) , min (z,m)), (min(n,z), max(0,z-n)) :
            if (z,t) not in d.keys():
                d[(z,t)] = (x,y)
                q.put((z,t))
            if (z==k or t ==k):
                pathh(d,(z,t))
                return 
    print("Khong dong duoc nuoc")

if __name__ == "__main__":
    bfs()