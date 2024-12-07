# bản chất đếm số đoạn trên đồ thị 

# n số học sinh , m là số muốn quan hệ 
parent = [0]*100005
sz = [1]*100005
def find(x):
    if(x == parent[x]):
         return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b): # gộp 2 thành phần
    a = find(a)
    b = find(b)
    if(a==b): 
        return False # chung 1 gốc
    
    # gộp vào cái có độ dài > hơn
    if(sz[a] > sz[b]): 
        parent[b] = a 
        sz[a] += sz[b]
    else:
        parent[a] = b 
        sz[b] += sz[a]
    return True

def init(n):
    for i in range(1,n+1):
        parent[i] = i

if __name__ =='__main__':
    n,m = map(int,input().split())
    init(n)
    for i in range(m):
        a,b= map(int,input().split())
        union(a,b)
    
    res =0
    maxx = -1e9
    for i in range(1,n+1):
        if(i == parent[i]):
            res+=1
            if(maxx < sz[i] ):
                maxx = sz[i]
    print(res)
    print(maxx)
