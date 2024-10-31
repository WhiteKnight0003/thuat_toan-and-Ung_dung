n = int(input())
list_num = list(map(int, input().split()))
sum_n = sum(list_num)
odd =0
even=0
for i in list_num:
    if i%2==0:
        even+=1
    else:
        odd+=1

# odd = even + 1 or even = odd+1 or even = odd
if(odd > even+1):
    sum_n -= (odd-(even+1))
elif (even > odd +1):
    sum_n -= (even-(odd+1) )
print(sum_n)
