m,n,p = map(int , input().split())
listA = list(map(int , input().split()))
listB = list(map(int , input().split()))
list_str = list(map(str, input().split()))

list_A = []
list_B = []
for item in list_str:
    if item[:4]=='PUSH' :
        print(item[5:])
        if(item[5:] =='A'):
            if(m==0):
                list_A.append(int(listB[n-1]))
                n-=1
            else:
                list_A.append(int(listA[m-1]))
                m-=1
        elif (item[5:] =='B'):
            if(n==0):
                list_A.append(int(listA[m-1]))
                m-=1
            else:
                list_B.append(int(listB[n-1]))
                n-=1
    elif(item[:3]=='POP'):
        print(item[4:])
        if(item[4:] =='A'):
            list_B.append(list_A.pop())
        elif (item[4:] =='B'):
            list_A.append(list_B.pop())

list_res = list_A+list_B
print(*list_res)