n = int(input())
res_str=''
while(n!=0):
    res_str+=str(n%2)
    n//=2
if(len(res_str) < 16):
    for i in range(16-len(res_str)):
        res_str+='0'
res_rever = res_str[::-1]
print(res_rever[:8])
print(res_rever[8:])
# print(res_str)


    