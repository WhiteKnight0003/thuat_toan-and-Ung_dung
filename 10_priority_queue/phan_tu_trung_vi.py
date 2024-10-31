# phần tử a[n/2]

# dùng 2 hàng đợi ưu tiên
# L : ưu tiên bé  
# mawxx của L phải luôn < R
# R : ưu tiên lớn
# vị trí i chẵn thêm vào R , lẻ thêm vào L
# max(L) là kết quả
from queue import PriorityQueue
L = PriorityQueue()
R = PriorityQueue()

n = int(input())
num = list(map(int, input().split()))[:n]

for i in range(0,len(num)) :
    if(i%2 ==0):
        L.put(-num[i])
    else:
        R.put(num[i])
    if(i>0 and -L.queue[0] > R.queue[0]):
        x = -L.get()
        y = R.get()
        R.put(x)
        L.put(-y)
    print(-L.queue[0], end =' ')

