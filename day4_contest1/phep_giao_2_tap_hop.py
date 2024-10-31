
input()
a = set(map(int,input().split()))
input()
b = set(map(int,input().split()))
c = a.intersection(b)
d = list(c)
d.sort()
print(*d)