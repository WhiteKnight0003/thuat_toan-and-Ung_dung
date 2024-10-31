from math import isqrt
try:
    t = int(input())
    while(t!=0):
        n = int(input())
        even = 1;
        odd =1;
        for i in range(2,isqrt(n)+1):
            if(n%i==0):
                cnt =0
                while(n%i==0):
                    cnt+=1
                    n//=i
                if cnt%2==0:
                    even*=i**(cnt/2)
                else:
                    even*=i**((cnt-1)/2)
                    odd*=i      
        if(n!=1):
            odd*=n
        print(f"{int(even)} {int(odd)}")
except EOFError: # Kết thúc chương trình khi hết input
    pass