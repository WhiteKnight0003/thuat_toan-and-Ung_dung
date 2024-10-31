import math
n = int(input())
DictL = {} # {cỡ, số lượng}
DictR = {}

while(n!=0):
    s = input()
    if(s[0]=='R'):
        DictR[s[1:]] = DictR.get(s[1:],0)+1
    elif s[0]=='L':
        DictL[s[1:]] = DictL.get(s[1:],0)+1
    n=n-1

res =0
for x in DictL.keys():
    if(DictR.get(x) != None):
        res+=min(DictR[x], DictL[x])
print(res)


# cách thầy tích
'''
L = {}
R = {}
for i in range(int(input())):
    s = input()
    x = int(s[1:])
    if s[0]=='L : L[x] = L.get(x,0)+1
    else:  R[x] = R.get(x,0)+1
    print(sum(min(L.get(i,0), R.get(i,0)) for i in range(101)))
'''