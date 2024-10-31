
from queue import LifoQueue
matrix = []

def DFS(u,v):
    global matrix
    q = LifoQueue()
    q.put((u,v))
    matrix[u][v]= 1 # đã xét
    while(q.qsize()):
        x,y = q.get()
        for i,j in (-1,0) , (1,0), (0,-1), (0,1): # trên dưới trái phải 
            if 0<=x+i<=m-1 and 0 <=y+j<=n-1 and matrix[x+i][y+j] ==0 :
                matrix[x+i][y+j] =1
                q.put((x+i,y+j))


if __name__ == "__main__":
    m ,n = map(int , input().split())
    #  m hàng , n cột

    # bao ma trận lại để k còn lo ra ngoài ma trận
    for i in range(m):
        row = list(map(int, input().split()))[:n]
        matrix.append(row)

    # xử lý các số 0 ở biên 
    for i in range(m):
        if matrix[i][0] ==0: DFS(i,0);
        if matrix[i][n-1] ==0: DFS(i,n-1);
    for j in range(n):
        if matrix[0][j] ==0: DFS(0,j);
        if matrix[m-1][j] ==0: DFS(m-1,j);
    count =0
    for i in range(0,m):
        for j in range(0,n):
            if(matrix[i][j] ==0):
                DFS(i,j)
                count +=1
    print(count)
    # print(*sorted(res))