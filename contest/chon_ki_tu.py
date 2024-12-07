n = int(input())
a = []
for i in range(n):
    a.append(input())

# tail
tail = a[n-1][len(a[n-1])-(n+1):] # lấy hết đoạn cuối của xâu n
# print(tail)
str =''
for i in range(n):
    str += min(a[i][i])
print(str+tail)