from math import isqrt
def scp(n):
    if(n>=0 and isqrt(n)*isqrt(n)==n):
        return True
    return False
n = int(input())
listNum = list(map(int, input().split()))[:n]
print(len(list(filter(lambda x: x%3!=0, listNum))))
print(len(list(filter(scp,listNum))))

print(len([1 for x,y in zip(listNum, listNum[1:]) if x!=0 and y%x==0]))

dc = len([x for x in listNum if x%2==0])
dl = n - dc
print(dc*(dc-1)//2 + dl*(dl-1)//2)
print(len([1 for x,y,z in zip(listNum, listNum[1:], listNum[2:]) if x<y<z]))