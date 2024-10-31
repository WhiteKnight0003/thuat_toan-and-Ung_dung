t = int(input())
while(t!=0):
    summ=0.0
    n = int(input())
    for i in range(n):
        a,k = map(int,input().split())
        summ += a/k
    if(summ==1):
        print('YES')
    else:
        print('NO')
    t-=1