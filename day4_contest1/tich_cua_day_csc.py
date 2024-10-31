
n, k = map(int, input().split())
mod = n%k
res=1
for i in range(n,0,-k):
        res*=i;
print(res)
# listNum = list(filter(lambda x: x%k==mod, range(1,n+1)))
# print(prod(listNum))