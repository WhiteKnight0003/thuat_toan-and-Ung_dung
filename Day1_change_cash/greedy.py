coin = [1000,2000,5000,10000,20000,50000,100000,500000,200000]
coin.sort(reverse = True)
res =0;
M = int(input())
for i in range(len(coin)):
    res+= M // coin[i]
    M%=coin[i]
if(M==0):
    print(res)
else:
    print("-1")
print()


