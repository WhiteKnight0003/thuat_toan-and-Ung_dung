n = int(input())
sum =0
mul=1
while(n):
    sum += n%10
    mul *= (n%10)
    n//=10
print(mul%sum)