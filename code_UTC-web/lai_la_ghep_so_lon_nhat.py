n = int(input())
num = list(map(str , input().split()))
D = {}
for i in num:
    D[int(i)] = i

res=''
for i in sorted(D.keys(), reverse=True):
    res += D[i].lstrip('0')
print(res)
