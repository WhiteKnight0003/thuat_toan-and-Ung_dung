parent = [0]*10005
sz = [1]*10005

def init(n):
    for i in range(1,n+1):
        parent[i]=i

def find(x):
    if(x == parent[x]):
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if(a == b):
        return False
    if(sz[a] > sz[b]):
        parent[b]= a
        sz[a] += sz[b]
    else:
        parent[a]= b
        sz[b] += sz[a]
    return True

if __name__ == "__main__":
    n,m= map(int, input().split())
    init(n)
    maxx = -1e9
    if(m==0):
        print(1)
    else:
        for i in range(m):
            a, b= map(int, input().split())
            union(a,b)
        
        for i in range(1,n+1):
            if i == parent[i]:
                if maxx < sz[i] :
                    maxx *= 1<< (sz[i]-1)
        print(maxx)

