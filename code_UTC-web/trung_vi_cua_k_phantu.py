n,k = map(int, input().split())
num = list(map(int, input().split()))[:n]

def means(list_n):
    list_n.sort()
    if(len(list_n)%2==0):
        return min(list_n[len(list_n)//2 -1] , list_n[len(list_n)//2 +1])
    return list_n[len(list_n)//2]

for i in range(n-k+1):
    print(num[i:k+i])
    print(means(list(num[i:k+i])))