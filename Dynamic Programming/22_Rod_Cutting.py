

"""
Rod cutting problem
Given length of rod N
[2,5,7,8,10]
 1 2 3 4 5
 
 Cut rod to maximize profit
N = 5
2+2+2+2+2 = 10
5+5+2 = 12
5+7 = 12

ALgo:
    Similar to unbounded knapsack conside N as w
    rephrasing it using rods to make N
"""

arr = [2,5,7,8,10]
N = 5

#Recursion
def rod_cutting(arr,i,N):
    if N == 0:
        return -float('inf')
    if i == 0:
        if i+1<=N: 
            return arr[0]*N             #i=0 means rod length 1 so how many rod needed to make N
        return 0
        


    not_take = rod_cutting(arr,i-1,N)
    rod_length = i+1
    take = -float('inf')
    if rod_length <= N:
        take = arr[i] + rod_cutting(arr,i,N-rod_length)

    return max(take, not_take)
print(rod_cutting(arr,N-1,N))

#Memoization
def rod_cutting(arr,i,N,dp):
    if N == 0:
        return -float('inf')
    if i == 0:
        if i+1<=N: 
            return arr[0]*N             #i=0 means rod length 1 so how many rod needed to make N
        return 0
        

    if dp[i][N] == -1:

        not_take = rod_cutting(arr,i-1,N, dp)
        rod_length = i+1
        take = -float('inf')
        if rod_length <= N:
            take = arr[i] + rod_cutting(arr,i,N-rod_length, dp)
        dp[i][N] = max(take, not_take)
    return dp[i][N]

dp = [[-1 for i in range(N+1)] for j in range(N)]
print(rod_cutting(arr,N-1,N, dp))

#Tabulation
dp = [[0 for i in range(N+1)] for j in range(N)]

for i in range(0,N+1):
    dp[0][i] = arr[0]*i

for i in range(1,N):
    for j in range(N+1):
        not_take = dp[i-1][j]
        take = -float('inf')
        if i+1 <= j:
            take = arr[i]+dp[i][j-(i+1)]
        dp[i][j] = max(take, not_take)
    
print(dp[N-1][N])

#Space Optimization
# We dont need previous array we only need left side 
dp = [0 for i in range(N+1)] 

for i in range(0,N+1):
    dp[i] = arr[0]*i

for i in range(1,N):
    for j in range(N+1):
        not_take = dp[j]
        take = -float('inf')
        if i+1 <= j:
            take = arr[i]+dp[j-(i+1)]
        dp[j] = max(take, not_take)    
print(dp[N])
