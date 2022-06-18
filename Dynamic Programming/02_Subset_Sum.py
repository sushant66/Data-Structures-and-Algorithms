"""
Subset Sum
find if subset with given sum 
for eg 2,3,5,8,10 sum = 11
        2,3,5 = 11
        3,8 = 11

if sum = 0 then for any n ans = True  (empty subset)
if arr = [] then for any sum ans = False  thats why if i == 0 False and j == 0 True
"""
#Recursion
arr = [2,3,5,8,10]
sum = 10

def subset_sum(arr,sum):
    if sum == 0:
        return True
    if len(arr) == 0:
        return False
    return subset_sum(arr[1:], sum-arr[0]) or subset_sum(arr[1:], sum)
print(subset_sum(arr,sum))

#Memoization
arr = [2,3,5,8,10]
sum = 10

def subset_sum(arr,sum, n,dp):
    if sum == 0:
        return True
    if len(arr) == 0:
        return False
    if dp[n][sum] == -1:
        dp[n][sum] = subset_sum(arr[1:], sum-arr[0], n-1, dp) or subset_sum(arr[1:], sum, n-1, dp)
    return dp[n][sum]

n = len(arr)
dp = [[-1 for i in range(sum+1)] for j in range(n+1)]
print(subset_sum(arr,sum, n, dp))

#Tabulation
arr = [2,3,5,8,10]
sum = 11

def subset_sum(arr,sum):
    n = len(arr)
    dp = [[0 for i in range(sum+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(sum+1):
            if i == 0:
                dp[i][j] = False
            if j == 0:
                dp[i][j] = True
            elif arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]   #(True or False)
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][sum]
print(subset_sum(arr,sum))


#Space Optimization
arr = [2,3,5,8,10]
sum = 15

def subset_sum(arr,sum):
    n = len(arr)
    dp = [False for i in range(sum+1)] 
    for i in range(n+1):
        temp = [0 for i in range(sum+1)] 
        for j in range(sum+1):
            if i == 0:
                temp[j] = False
            if j == 0:
                temp[j] = True
            elif arr[i-1] <= j:
                temp[j] = dp[j-arr[i-1]] or dp[j]   #(True or False)
            else:
                temp[j] = dp[j]
        dp = temp
    return dp[sum]
print(subset_sum(arr,sum))
