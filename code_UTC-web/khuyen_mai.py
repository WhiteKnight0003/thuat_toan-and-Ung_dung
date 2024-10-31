n = int(input())
list_num = list(map(int, input().split()))[:n]
sum_n = sum(list_num)
res=0
if n%3==0:
    while(n!=0):
        sum1 = sum_n - min(list_num[n-3:n])
        sum2 = sum_n - sum(x//3 for x in list_num[n-3:n])
        if(sum1 < sum2 ):
            res+=sum1
        else:
            res+=sum2
        n-=3
else:
    while(n>3):
        sum1 = sum_n - min(list_num[n-3:n])
        sum2 = sum_n - sum(x//3 for x in list_num[n-3:n])
        if(sum1 < sum2 ):
            res+=sum1
        else:
            res+=sum2
        n-=3
        print(sum_n, sum1, sum2, res)
    res-=  sum(x//3 for x in list_num[0:n])
print(res)