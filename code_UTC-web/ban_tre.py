n , k = map(int, input().split())
list_num = list(map(int,input().split()))[:n]
res =0
for i in list_num:
    res += i//k
print(3*k*res)
    