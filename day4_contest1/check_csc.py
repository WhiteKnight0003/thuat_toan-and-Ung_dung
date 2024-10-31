n = int(input())
listNum = list(map(int, input().split()))
congsai = listNum[1]- listNum[0]

b = [x-y for y,x in zip(listNum,listNum[1:])]
s = set(b)
if len(s)==1:
    print(f"Day la day cap so cong voi cong sai {b[0]}")
else:
    print("Day khong la day cap so cong")