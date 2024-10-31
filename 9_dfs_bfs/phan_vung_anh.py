# from queue import LifoQueue


# matrix = []

# def DFS(u,v):
#     global matrix
#     q = LifoQueue()
#     q.put((u,v))
#     matrix[u][v]= 1 # đã xét
#     count =1
#     while(q.qsize()):
#         x,y = q.get()
#         for i in range(-1,2):
#             for j in range(-1,2):
#                 if matrix[x+i][y+j] ==0:
#                     matrix[x+i][y+j] =1
#                     q.put((x+i,y+j))
#                     count+=1
#     return count


# if __name__ == "__main__":
#     m ,n = map(int , input().split())
#     #  m hàng , n cột

#     # bao ma trận lại để k còn lo ra ngoài ma trận
#     matrix.append([1]*(m+2))
#     for i in range(m):
#         row = list(map(int, input().split()))[:n]
#         matrix.append([1] + row +[1])
#     matrix.append([1]*(m+2))

#     res =[]
#     for i in range(1,m+1):
#         for j in range(1,n+1):
#             if(matrix[i][j] ==0):
#                 if(matrix[i][j] ==0):
#                     res.append(DFS(i,j))
#     print(len(res))
#     print(*sorted(res))


from queue import LifoQueue
matrix = []

def DFS(u,v):
    global matrix
    q = LifoQueue()
    q.put((u,v))
    matrix[u][v]= 1 # đã xét
    count =1
    while(q.qsize()):
        x,y = q.get()
        for i in range(-1,2):
            for j in range(-1,2):
                if 0<=x+i<=m-1 and 0 <=y+j<=n-1 and matrix[x+i][y+j] ==0 :
                    matrix[x+i][y+j] =1
                    q.put((x+i,y+j))
                    count+=1
    return count


if __name__ == "__main__":
    m ,n = map(int , input().split())
    #  m hàng , n cột

    # bao ma trận lại để k còn lo ra ngoài ma trận
    for i in range(m):
        row = list(map(int, input().split()))[:n]
        matrix.append(row)

    res =[]
    for i in range(0,m):
        for j in range(0,n):
            if(matrix[i][j] ==0):
                res.append(DFS(i,j))
    print(len(res))
    print(*sorted(res))