# num = []
# sum =0
# try:
#     while True:
#         if(input().strip()==''):
#             break
#         sum+=int(input())
#         sum%=(1000000007)
# except EOFError:
#     pass

# print((sum+1000000007)%(1000000007))

# import sys

# # Đọc tất cả đầu vào từ người dùng
# num = list(map(int, sys.stdin.read().splitlines()))
# print("Tổng của dãy số là:", sum(num))
# sum=0
# for i in num:
#     sum += i
#     sum%=(1e9+7)
# print(sum%(1e9+7))