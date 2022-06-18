"""
Given weights and values find max values you can get for a given weight limit
wt = [3,5,6]
val = [30,40,60]
w = 9

ans = 30+60 = 90

"""


wt = [3,5,6]
val = [30,40,60]
w = 9

# Recursion
def knapsack(wt,val,w, i):
    if w == 0:
        return 0
    if i == 0:
        if wt[0] <= w:
            return val[0]
        else:
            return 0
    

    not_take = knapsack(wt, val, w, i-1)
    take = -float('inf')
    if wt[i]<=w:
        take = val[i]+knapsack(wt,val,w-wt[i], i-1)
    return max(not_take, take)


print(knapsack(wt,val,w,len(wt)-1))


# Memoization
def knapsack(wt,val,w, i, dp):
    if w == 0:
        return 0
    if i == 0:
        if wt[0] <= w:              #for all values of w > wt[0]
            return val[0]
        else:
            return 0
    
    if dp[i][w] == -1:
        not_take = knapsack(wt, val, w, i-1, dp)
        take = -float('inf')
        if wt[i]<=w:
            take = val[i]+knapsack(wt,val,w-wt[i], i-1, dp)
        dp[i][w] = max(not_take, take)
    return dp[i][w] 

dp = [[-1 for i in range(w+1)] for j in range(len(wt))]
print(knapsack(wt,val,w,len(wt)-1, dp))

# Tabulation
dp = [[0 for i in range(w+1)] for j in range(len(wt))]

for i in range(wt[0], w+1):    #for all values of wt[0] to w i.e w> wt[0]
    dp[0][i] = val[0]

for i in range(1,len(wt)):
    for j in range(w+1):
        if wt[i]<=j:
            dp[i][j] = max(val[i]+dp[i-1][j-wt[i]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[len(wt)-1][w])

#Space Optimization
"""
We only need left elements and not right elements
for eg
dp[i-1][j-wt[i]]  -- j-wt[i] will always be at the left and hence we can drop temp array

dp[j] = max(val[i]+dp[j-wt[i]], dp[j])   

In all other cases it was j-arr[i] and it can be at right or left so we needed temp array

"""
dp = [0 for i in range(w+1)]

for i in range(wt[0], w+1):    #for all values of wt[0] to w i.e w> wt[0]
    dp[i] = val[0]

for i in range(1,len(wt)):
    for j in range(w+1):
        if wt[i]<=j:
            dp[j] = max(val[i]+dp[j-wt[i]], dp[j])
print(dp[w])
