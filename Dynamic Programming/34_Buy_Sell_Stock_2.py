
"""
Buy sell stock II

Buy and sell stocks to maximize profit
eg:
    arr = 7 1 5 3 6 4
    
    buy at 1 sell at 5 = 4
    byt at 3 sell at 6 = 3 
    total = 7

"""
arr = [7, 1, 5, 3, 6,4]

#Recursion
def buy_sell(arr,i,buy):
    if i == len(arr):
        return 0
    

    if buy:
        return max(-arr[i] + buy_sell(arr,i+1,0), buy_sell(arr,i+1,1))  #money going (peak-valley)
    else:
        return max(arr[i]+buy_sell(arr,i+1,1), buy_sell(arr,i+1,0))         #money coming

print(buy_sell(arr,0,1))


#Memoization
def buy_sell(arr,i,buy, dp):
    if i == len(arr):
        return 0
    
    if dp[i][buy] == -1:

        if buy:
            dp[i][buy] = max(-arr[i] + buy_sell(arr,i+1,0,dp), buy_sell(arr,i+1,1,dp))  #money going (peak-valley)
        else:
            dp[i][buy] = max(arr[i] + buy_sell(arr,i+1,1,dp), buy_sell(arr,i+1,0,dp))         #money coming
    return dp[i][buy]

dp = [[-1 for j in range(2)] for i in range(len(arr))]
print(buy_sell(arr,0,1,dp))

#Tabulation
n = len(arr)
dp = [[0 for j in range(2)] for i in range(n+1)]

dp[n][0] = dp[n][1] = 0

for i in range(n-1,-1,-1):
    for j in range(2):
        if j:
            dp[i][j] = max(-arr[i]+dp[i+1][0], dp[i+1][1])
        else:
            dp[i][j] = max(arr[i]+dp[i+1][1], dp[i+1][0])
print(dp[0][1])

#Space Optimization
dp = [0 for j in range(2)]

for i in range(n-1,-1,-1):
    temp = [0 for j in range(2)]
    for j in range(2):
        if j:
            temp[j] = max(-arr[i]+dp[0], dp[1])
        else:
            temp[j] = max(arr[i]+dp[1], dp[0])
    dp = temp
print(dp[1])

prev_buy = 0
prev_not_buy = 0
for i in range(n-1,-1,-1):
    curr_buy = 0
    curr_not_buy = 0

    curr_not_buy = max(arr[i]+prev_buy, prev_not_buy)
    curr_buy = max(-arr[i]+curr_not_buy, curr_buy)

    prev_buy = curr_buy
    prev_not_buy = curr_not_buy

print(prev_buy)


