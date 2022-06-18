
"""
Buy sell stock III

Buy and sell stocks to maximize profit you can do at most 2 transaction
eg:
    arr =  3 3 5 0 0 3 1 4
    
    buy at 3 sell at 5 = 2
    byt at 0 sell at 4 = 4 
    total = 6

"""
arr = [3, 3, 5, 0, 0, 3, 1, 4]

#Recursion
def buy_sell(arr,i,buy,cap):
    if i == len(arr) or cap == 0:
        return 0
    

    if buy:
        return max(-arr[i] + buy_sell(arr,i+1,0,cap), buy_sell(arr,i+1,1,cap))  #money going (peak-valley)
    else:
        return max(arr[i]+buy_sell(arr,i+1,1, cap-1), buy_sell(arr,i+1,0,cap))         #money coming

print(buy_sell(arr,0,1,2))


#Memoization
def buy_sell(arr,i,buy,cap,dp):
    if i == len(arr) or cap==0:
        return 0
    
    if dp[i][buy][cap] == -1:

        if buy:
            dp[i][buy][cap] = max(-arr[i] + buy_sell(arr,i+1,0,cap,dp), buy_sell(arr,i+1,1,cap,dp))  #money going (peak-valley)
        else:
            dp[i][buy][cap] = max(arr[i] + buy_sell(arr,i+1,1,cap-1,dp), buy_sell(arr,i+1,0,cap,dp))         #money coming
    return dp[i][buy][cap]

dp = [[[-1 for k in range(3)] for j in range(2)] for i in range(len(arr))]
print(buy_sell(arr,0,1,2,dp))

#Tabulation
n = len(arr)
dp = [[[0 for k in range(3)] for j in range(2)] for i in range(n+1)]

dp[n][0][0] = dp[n][1][0] = 0

for i in range(n-1,-1,-1):
    for j in range(2):
        for k in range(1,3):
            if j:
                dp[i][j][k] = max(-arr[i]+dp[i+1][0][k], dp[i+1][1][k])
            else:
                dp[i][j][k] = max(arr[i]+dp[i+1][1][k-1], dp[i+1][0][k])
                
print(dp[0][1][2])

#Space Optimization
dp = [[0 for k in range(3)] for j in range(2)]

for i in range(n-1,-1,-1):
    temp = [[0 for x in range(3)] for y in range(2)]
    for j in range(2):
        for k in range(1,3):
            if j:
                temp[j][k] = max(-arr[i]+dp[0][k], dp[1][k])
            else:
                temp[j][k] = max(arr[i]+dp[1][k-1], dp[0][k])
    dp = temp
print(dp[1][2])

#METHOD  2
# remove buy and have 4 transactions  
# B S B S  -- for even we buy for odd we sell  and we start from 0

n = len(arr)
dp = [[0 for j in range(5)] for i in range(n+1)]

for i in range(n-1,-1,-1):
    for j in range(3,-1,-1):
        if j%2 == 0:
            dp[i][j] = max(-arr[i]+dp[i+1][j+1], dp[i+1][j])
        else:
            dp[i][j] = max(arr[i]+dp[i+1][j+1], dp[i+1][j])
                
print(dp[0][0])

n = len(arr)
dp = [0 for j in range(5)] 

for i in range(n-1,-1,-1):
    temp = [0 for k in range(5)] 
    for j in range(3,-1,-1):
        if j%2 == 0:
            temp[j] = max(-arr[i]+dp[j+1], dp[j])
        else:
            temp[j] = max(arr[i]+dp[j+1], dp[j])
    dp = temp
                
print(dp[0])



