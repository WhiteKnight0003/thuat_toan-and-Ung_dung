def solve_scooby_path(n, stones):
    dp = [float('inf')] * n
    dp[0] = 0  
    for i in range(n):
        if stones[i] == 1:
            continue

        if i + 1 < n and stones[i + 1] == 0:
            dp[i + 1] = min(dp[i + 1], dp[i] + 1)
            
        # Thử nhảy qua 1 hòn đá
        if i + 2 < n and stones[i + 2] == 0:
            dp[i + 2] = min(dp[i + 2], dp[i] + 1)
    
    # Nếu không thể đến đích
    if dp[n-1] == float('inf'):
        return "khong qua duoc suoi"
    
    return dp[n-1]

# Đọc input
n = int(input())
stones = list(map(int, input().split()))

# In kết quả
print(solve_scooby_path(n, stones))