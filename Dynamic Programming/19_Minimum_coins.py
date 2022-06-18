

"""
Minimum coins to make a target
eg 1,2,3 t = 8
3+3+2 = 8 so ans = 3


For infite supply stand at the same index
"""
arr = [1,2,3]
t = 8

#Recursion
def min_coins(arr, t, i):
    if i == 0:
        if t%arr[0] == 0: return t//arr[0]
        return float('inf')

    
    not_take = min_coins(arr,t,i-1)
    take = float('inf')
    if arr[i]<=t:
        take = 1 + min_coins(arr,t-arr[i],i)
    return min(not_take, take)

print(min_coins(arr,t,len(arr)-1))


#Memoization
dp = [[-1 for i in range(t+1)] for j in range(len(arr))]

def min_coins(arr, t, i, dp):
    if i == 0:
        if t%arr[0] == 0: return t//arr[0]
        return float('inf')

    if dp[i][t] == -1:
        not_take = min_coins(arr,t,i-1, dp)
        take = float('inf')
        if arr[i]<=t:
            take = 1 + min_coins(arr,t-arr[i],i, dp)
        dp[i][t] = min(not_take, take)
    return dp[i][t]

print(min_coins(arr,t,len(arr)-1,dp))

#Tabulation
dp = [[float('inf') for i in range(t+1)] for j in range(len(arr))]

for i in range(len(arr)):
    for j in range(t+1):
        if i == 0:
            if j%arr[0] == 0:
                dp[i][j] = j//arr[0]
        else:
            not_take = dp[i-1][j]
            take = float('inf')
            if arr[i]<=j:
                take = 1 + dp[i][j-arr[i]]
            dp[i][j] = min(not_take, take)
print(dp[len(arr)-1][t])


#Space Optimization
dp = [float('inf') for i in range(t+1)] 

for i in range(len(arr)):
    temp = [float('inf') for i in range(t+1)] 
    for j in range(t+1):
        if i == 0:
            if j%arr[0] == 0:
                temp[j] = j//arr[0]
        else:
            not_take = dp[j]
            take = float('inf')
            if arr[i]<=j:
                take = 1 + temp[j-arr[i]]
            temp[j] = min(not_take, take)
    dp = temp
print(dp[t])

