"""

	Check if there is a subset whose sum is equal to K
"""


#Recursive
arr = [3, 34, 4, 12, 5, 2]
k = 9
def subset_sum(arr, k):
    if len(arr) == 0 or k < 0:
        return False
    if k == 0:
        return True
    
    return subset_sum(arr[1:], k) or subset_sum(arr[1:], k-arr[0])

print(subset_sum(arr,k))


#Memoization
n = len(arr)
dp = [[-1 for i in range(k+1)] for j in range(n+1)]
def subset_sum(arr, k, n):
    if len(arr) == 0 or k < 0:
        return False
    if k == 0:
        return True
    
    if dp[n][k] == -1:
        dp[n][k] = subset_sum(arr[1:], k, n-1) or subset_sum(arr[1:], k-arr[0], n-1) 
    return dp[n][k]

print(subset_sum(arr,k, n))


#Tabulation
n = len(arr)
dp = [[False for i in range(k+1)] for j in range(n+1)]

for i in range(n+1):
    for j in range(k+1):
        if j == 0:
            dp[i][j] = True
        elif i == 0:
            dp[i][j] = False
        else:
            dp[i][j] = dp[i-1][j] or dp[i][j-arr[i-1]]
print(dp[n][k])


#Space optimization
n = len(arr)

dp = [False for i in range(k+1)]

for i in range(n+1):
    temp = [False for j in range(k+1)]
    for j in range(k+1):
        if j == 0:
            temp[j] = True
        elif i == 0:
            temp[j] = False
        else:
            temp[j] = dp[j] or temp[j-arr[i-1]]
    dp = temp
print(dp[k])
