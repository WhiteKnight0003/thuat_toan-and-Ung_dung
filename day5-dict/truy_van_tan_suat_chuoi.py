n = int(input())
dictS = {}
while(n!=0):
    s = input()
    dictS[s] = dictS.get(s,0)+1
    n=n-1

m = int(input())
while(m!=0):
    s = input()
    if(dictS.get(s) != None):
        print(dictS[s])
    else:
        print("0")
    m=m-1

