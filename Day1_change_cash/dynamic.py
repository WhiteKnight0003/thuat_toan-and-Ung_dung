from math import *
def count(coin,n,M):
    table = [[0 for j in range(M+1)] for i in range(n+1)]

    table[0][0] = 0  #Không cần đồng xu nào để tạo ra số tiền 0.
    
    for j in range(1,M+1):
        table[0][j] = 10**9 #Không thể tạo ra số tiền dương nào nếu không có đồng xu nào

    for i in range(1,n+1):
        for j in range(M+1):
            if j< coin[i-1] :
                table[i][j]= table[i-1][j]
            else:
                table[i][j] = min(table[i-1][j], 1+table[i][j-coin[i-1]])
    
    return table[n][M]

if __name__ == "__main__":
    M = int(input())
    coin = [10000,20000,50000,100000,200000,500000,1000,2000,5000]
    n = len(coin)
    res = count(coin,n,M)
    if( res == 10**9):
        print("-1")
    else :
        print(res)
