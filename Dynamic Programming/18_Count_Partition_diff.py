"""
Count partitions with given difference

Algo : same as count subset sum where target = total-diff/2
"""
arr = [5,2,6,4]
k = 3

#Recursion
if sum(arr)-k < 0 or (sum(arr)-k)%2 != 0:
    print(0)
def count_partition_diff(arr,k, n):
    if n == 0:              # remove if sum == 0 as it will skip zeros present in array
        if k == 0 and arr[0] == 0:     #2 possibility as sum has become 0 due to somebody and the current element is also 0
            return 2
        if k == 0 or arr[0] == k:       #Either sum has become 0 or the current element will make sum 0
            return 1
        return 0

    not_take = count_partition_diff(arr, k, n-1)
    take = 0
    if arr[n]<=k:
        take = count_partition_diff(arr, k-arr[n], n-1)
    return take + not_take

n = len(arr)-1
d = int((sum(arr)-k)/2)             # s1-s2 = k     s1= total-s2   total-2s2 = k (total-k)/2 = s2
print(count_partition_diff(arr,d, n))


#Memoization
def count_partition_diff(arr,k, n,dp):
    if sum == 0:
        return 1
    if n == 0:              # remove if sum == 0 as it will skip zeros present in array
        if k == 0 and arr[0] == 0:     #2 possibility as sum has become 0 due to somebody and the current element is also 0
            return 2
        if k == 0 or arr[0] == k:       #Either sum has become 0 or the current element will make sum 0
            return 1
        return 0

    if dp[n][k] == -1:
        not_take = count_partition_diff(arr, k, n-1,dp)
        take = 0
        if arr[n]<=k:
            take = count_partition_diff(arr, k-arr[n], n-1,dp)
        dp[n][k] = take + not_take
    return dp[n][k]

n = len(arr)-1
dp = [[-1 for i in range(d+1)] for j in range(n+1)]
print(count_partition_diff(arr,d, n, dp))

#Tabulation
def count_partition_diff(arr, target):
    n = len(arr)
    dp = [[0 for i in range(target+1)] for j in range(n+1)]
    if arr[0] == 0:
        dp[0][0] = 2            #sum is 0 and num is also 0
    else:
        dp[0][0] = 1
    if arr[0]!=0 and arr[0] <= target: dp[0][arr[0]] = 1    #dp[0][arr[0]] arr[0] indicates sum so for that value it will be 1   
    for i in range(1,n):
        for j in range(target+1):
            if arr[i] <= j:
                dp[i][j] = dp[i-1][j-arr[i]] + dp[i-1][j]   
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n-1][target]

print(count_partition_diff(arr, d))

#Space optimize
def count_partition_diff(arr, target):
    n = len(arr)
    dp = [0 for i in range(target+1)]
    if arr[0] == 0:
        dp[0] = 2            #sum is 0 and num is also 0
    else:
        dp[0] = 1
    if arr[0]!=0 and arr[0] <= target: dp[arr[0]] = 1
    for i in range(1, n):
        temp = [0 for k in range(target+1)]
        for j in range(target+1):
            if arr[i] <= j:
                temp[j] = dp[j-arr[i]] + dp[j]   
            else:
                temp[j] = dp[j]
        dp = temp
    return dp[target]

print(count_partition_diff(arr, d))

