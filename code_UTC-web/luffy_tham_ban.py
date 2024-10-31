import statistics
n = int(input())
num_n = list(map(int, input().split()))[:n]
num_n.sort()
means =0
if(n%2!=0): means = num_n[n//2]
else : means = num_n[n//2 -1]
summ=0
for i in num_n:
    summ+= abs(means-i)
print(summ)