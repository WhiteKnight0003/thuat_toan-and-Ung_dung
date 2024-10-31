
list_num = list(map(int, input().split()))
sum_n = sum(list_num)
min_n = min(list_num)
max_n = max(list_num)

x = sum_n-max_n- min_n
if x+ min_n != max_n:
    print('No')
else :
    print('Yes')