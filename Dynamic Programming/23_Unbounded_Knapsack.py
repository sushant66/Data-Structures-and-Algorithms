"""
Unbounded knapsack
Same as 0/1 except you have infinite supply
eg  wt = [2,4,6]
    val = [5,11,13]
    w = 10
    5 + 11*2 = 27
"""

wt = [2,4,6]
val = [5,11,13]

w = 10

#Recursion
def unbounded_knapsack(wt,val,w,n):
    if w == 0:
        return -float('inf')
    if n == 0:
        if wt[0] <= w:
            return val[0] * (w//wt[0])
        return 0
    
    # print(w)
    not_take = unbounded_knapsack(wt,val,w,n-1)
    take = -float('inf')
    if wt[n]<=w:
        take = val[n] + unbounded_knapsack(wt,val,w-wt[n],n)
    return max(not_take,take)

print(unbounded_knapsack(wt,val,w,len(wt)-1))


#Memoization
def unbounded_knapsack(wt,val,w,n,dp):
    if w == 0:
        return -float('inf')
    if n == 0:
        if wt[0] <= w:              #w varies 
            return val[0] * (w//wt[0])
        return 0
    if dp[n][w] == -1:
        not_take = unbounded_knapsack(wt,val,w,n-1,dp)
        take = -float('inf')
        if wt[n]<=w:
            take = val[n] + unbounded_knapsack(wt,val,w-wt[n],n,dp)
        dp[n][w] = max(not_take,take)
    return dp[n][w]

dp = [[-1 for i in range(w+1)] for j in range(len(wt))]
print(unbounded_knapsack(wt,val,w,len(wt)-1,dp))


#Tabulation
n = len(wt)
dp = [[0 for i in range(w+1)] for j in range(n)]

for j in range(0,w+1):
    dp[0][j] = val[0] * (j//wt[0])

for i in range(1,n):
    for j in range(w+1):
        not_take = dp[i-1][j]
        take = -float('inf')
        if wt[i] <= j:
            take = val[i] + dp[i][j-wt[i]]
        dp[i][j] = max(not_take, take)

print(dp[n-1][w])

#Space Optimization
n = len(wt)
dp = [0 for i in range(w+1)]

for j in range(0,w+1):
    dp[j] = val[0] * (j//wt[0])

for i in range(1,n):
    temp = [0 for i in range(w+1)]
    for j in range(w+1):
        not_take = dp[j]
        take = -float('inf')
        if wt[i] <= j:
            take = val[i] + temp[j-wt[i]]
        temp[j] = max(not_take, take)
    dp = temp

print(dp[w])

#More Space Optimization
# We dont need previous we only need left side data as j-wt[i] will always lie on left
# we dont need previous left side elements we just need previous curr element so we can overwrite it

n = len(wt)
dp = [0 for i in range(w+1)]

for j in range(0,w+1):
    dp[j] = val[0] * (j//wt[0])

for i in range(1,n):
    for j in range(w+1):
        not_take = dp[j]            #just need previous rows cur index element
        take = -float('inf')
        if wt[i] <= j:
            take = val[i] + dp[j-wt[i]]
        dp[j] = max(not_take, take)     #overwriting the index

print(dp[w])




