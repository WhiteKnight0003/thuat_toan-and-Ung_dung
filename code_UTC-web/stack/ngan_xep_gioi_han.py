n , k = map(int, input().split())
stack = []

for i in range(1,k+1):
    list_n = list(map(str, input().split()))
    if(list_n[0]=='PUSH' and len(stack) <n):
        stack.append(int(list_n[1]))
    elif list_n[0]=='POP':
        stack.pop();

list_res = []
while(len(stack) !=0):
    list_res.append(stack.pop())
print(*list_res)
