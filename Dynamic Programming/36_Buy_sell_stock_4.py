"""
Buy sell stock II

Buy and sell stocks to maximize profit with at most k transaction

Algo: Same as buy sell stock 3 just put k value in cap
"""

#Space Optimized
n = len(prices)
dp = [[0 for i in range(k+1)] for j in range(2)]

for i in range(n-1,-1,-1):
    temp = [[0 for x in range(k+1)] for y in range(2)]
    for j in range(2):
        for k in range(1,k+1):
            if j:
                temp[j][k] = max(-prices[i]+dp[0][k], dp[1][k])
            else:
                temp[j][k] = max(prices[i]+dp[1][k-1], dp[0][k])
    dp = temp
return dp[1][k]


#Space Optimized Method 2
n = len(prices)
dp = [0 for j in range(2*k+1)] 

for i in range(n-1,-1,-1):
    temp = [0 for x in range(2*k+1)] 
    for j in range(2*k-1,-1,-1):
        if j%2 == 0:
            temp[j] = max(-prices[i]+dp[j+1], dp[j])
        else:
            temp[j] = max(prices[i]+dp[j+1], dp[j])
    dp = temp

return dp[0]
