n = int(input())
list_num = list(map(int , input().split()))[:n]
print(*list(filter(lambda x: x!=0 ,list_num)))