from itertools import accumulate
#  trong c++ có hàm partial_sum để tính tổng tích lũy thì trong python có accumulate
m,n = map(int,input().split())
list_num = list(map(int, input().split()))
res =[0] + list(accumulate(list_num))
for i in range(n): # 0, n-1
    x,y =map(int, input().split())
    print(res[y]-res[x-1])
