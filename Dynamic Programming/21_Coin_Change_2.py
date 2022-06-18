

"""
Coin change 2

Number of ways to make a target with infinite supply of coins
eg 1,2,3 = 4
 1+1+1+1 = 4
 1+2+1= 4
 2+2 = 4
 1+3 = 4
    4 ways

For infite supply stand at the same index
"""
arr = [1,2,3]
t = 4

#Recursion
def coin_change_2(arr, t, i):
    if i == 0:
        if t%arr[0] == 0: return 1
        return 0

    
    not_take = coin_change_2(arr,t,i-1)
    take = 0
    if arr[i]<=t:
        take = coin_change_2(arr,t-arr[i],i)
    return not_take+take

print(coin_change_2(arr,t,len(arr)-1))


#Memoization
dp = [[-1 for i in range(t+1)] for j in range(len(arr))]

def coin_change_2(arr, t, i, dp):
    if i == 0:
        if t%arr[0] == 0: return 1
        return 0

    if dp[i][t] == -1:
        not_take = coin_change_2(arr,t,i-1, dp)
        take = 0
        if arr[i]<=t:
            take = coin_change_2(arr,t-arr[i],i, dp)
        dp[i][t] = not_take + take
    return dp[i][t]

print(coin_change_2(arr,t,len(arr)-1,dp))

#Tabulation
dp = [[0 for i in range(t+1)] for j in range(len(arr))]

for i in range(len(arr)):
    for j in range(t+1):
        if i == 0:
            if j%arr[0] == 0:
                dp[i][j] = 1
        else:
            not_take = dp[i-1][j]
            take = 0
            if arr[i]<=j:
                take = dp[i][j-arr[i]]
            dp[i][j] = not_take + take
print(dp[len(arr)-1][t])


#Space Optimization
dp = [0 for i in range(t+1)] 

for i in range(len(arr)):
    temp = [0 for i in range(t+1)] 
    for j in range(t+1):
        if i == 0:
            if j%arr[0] == 0:
                temp[j] = 1
        else:
            not_take = dp[j]
            take = 0
            if arr[i]<=j:
                take = temp[j-arr[i]]
            temp[j] = not_take + take
    dp = temp
print(dp[t])

