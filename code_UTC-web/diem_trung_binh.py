n = int(input())
D = {}
res =0
while(n>0):
    x,y = map(str , input().split());
    y = int(y)
    res+=y
    D[x]=y
    n-=1
res /= len(D)
res_num = round(res, 1)
print(f"DIEM TRUNG BINH {res_num}")
for i in D.keys():
    if(D[i]>res):
        print(i, D[i])