"""
Count no of subset with given sum

Algo : same as subset sum (replace or with +  (add all leaf node answers))
"""


#Recursion
def count_subset_sum(arr,sum, n):
    if sum == 0:
        return 1
    if n == 0:
        if arr[0] == sum:
            return 1
        return 0

    not_take = count_subset_sum(arr, sum, n-1)
    take = 0
    if arr[n]<=sum:
        take = count_subset_sum(arr, sum-arr[n], n-1)
    return take + not_take

n = len(arr)-1
print(count_subset_sum(arr,sum, n))

#Memoization
def count_subset_sum(arr,sum, n,dp):
    if sum == 0:
        return 1
    if n == 0:
        if arr[0] == sum:
            return 1
        return 0

    if dp[n][sum] == -1:
        not_take = count_subset_sum(arr, sum, n-1,dp)
        take = 0
        if arr[n]<=sum:
            take = count_subset_sum(arr, sum-arr[n], n-1,dp)
        dp[n][sum] = take + not_take
    return dp[n][sum]

n = len(arr)-1
dp = [[-1 for i in range(sum+1)] for j in range(n+1)]
print(count_subset_sum(arr,sum, n, dp))

#Tabulation
arr = [1,5,11,5]

def count_subset_sum(arr, target):
    n = len(arr)
    dp = [[0 for i in range(target+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(target+1):
            if i == 0:
                dp[i][j] = 0
            if j == 0:
                dp[i][j] = 1
            elif arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]   
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][target]

print(count_subset_sum(arr, 11))

#Space optimize
arr = [1,5,11,5]

def count_subset_sum(arr, target):
    n = len(arr)
    dp = [0 for i in range(target+1)]
    for i in range(n+1):
        temp = [0 for k in range(target+1)]
        for j in range(target+1):
            if i == 0:
                temp[j] = 0
            if j == 0:
                temp[j] = 1
            elif arr[i-1] <= j:
                temp[j] = dp[j-arr[i-1]] + dp[j]   
            else:
                temp[j] = dp[j]
        dp = temp
    return dp[target]

print(count_subset_sum(arr, 11))

#If arr consist of 0's also then ans = ans*pow(2,n) n- no of zeros
arr = [0,0,1]
sum = 1
arr = [1,5,11,5]
sum = 11
#Memmoization
def count_subset_sum(arr,sum, n,dp):
    if n == 0:              # remove if sum == 0 as it will skip zeros present in array
        if sum == 0 and arr[0] == 0:     #2 possibility as sum has become 0 due to somebody and the current element is also 0
            return 2
        if sum == 0 or arr[0] == sum:       #Either sum has become 0 or the current element will make sum 0
            return 1
        return 0
    if dp[n][sum] == -1:
        not_take = count_subset_sum(arr, sum, n-1,dp)
        take = 0
        if arr[n]<=sum:
            take = count_subset_sum(arr, sum-arr[n], n-1,dp)
        dp[n][sum] = take + not_take
    return dp[n][sum]

n = len(arr)-1
dp = [[-1 for i in range(sum+1)] for j in range(n+1)]
print(count_subset_sum(arr,sum, n, dp))

