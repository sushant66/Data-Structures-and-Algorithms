"""
Buy Sell Stock with Cooldown
Maximize the profit with a condition that you cannot buy on exact next day after selling

prices = [1,2,3,0,2]
Output: 3

Buy at 1 sell at 2  = 1
cooldown on 3 
buy at 0 sell at 2 = 2

Algo: Same as buy sell stock 2 except after selling jump to i+2

"""

prices = [1,2,3,0,2]

#Recursion
def buy_sell(prices,i,buy):
    if i >= len(prices):
        return 0
    
    if buy:
        return max(-prices[i] + buy_sell(prices,i+1,0), buy_sell(prices,i+1,1))
    return max(prices[i] + buy_sell(prices,i+2,1), buy_sell(prices,i+1,0))

print(buy_sell(prices,0,1))

#Memoization
def buy_sell(prices,i,buy,dp):
    if i >= len(prices):
        return 0
    
    if dp[i][buy] == -1:
    
        if buy:
            dp[i][buy] = max(-prices[i] + buy_sell(prices,i+1,0,dp), buy_sell(prices,i+1,1,dp))
        else:
            dp[i][buy] = max(prices[i] + buy_sell(prices,i+2,1,dp), buy_sell(prices,i+1,0,dp))
    return dp[i][buy]

n = len(prices)
dp = [[-1 for i in range(2)] for j in range(n)]
print(buy_sell(prices,0,1,dp))

#Tabulation
n = len(prices)
dp = [[0 for i in range(2)] for j in range(n+2)]

for i in range(n-1,-1,-1):
    for j in range(2):
        if j:
            dp[i][j] = max(-prices[i]+dp[i+1][0], dp[i+1][1])
        else:
            dp[i][j] = max(prices[i]+dp[i+2][1], dp[i+1][0])

print(dp[0][1])

#METHOD 2

n = len(prices)
dp = [[0 for i in range(2)] for j in range(n+2)]

for i in range(n-1,-1,-1):
    dp[i][1] = max(-prices[i]+dp[i+1][0], dp[i+1][1])
    dp[i][0] = max(prices[i]+dp[i+2][1], dp[i+1][0])

print(dp[0][1])
