n = int(input())
L=[]
L.append(n)
while(True):
    if n==1:
        break
    elif n%2==1:
        L.append(3*n+1)
        n = 3*n+1
    else:
        L.append(n//2)
        n = n//2
print(len(L), *L, sep = " ")
