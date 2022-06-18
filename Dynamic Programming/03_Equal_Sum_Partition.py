
"""
Equal Sum Partition 
arr = [1,5,11,5]      True
    1,5,5 - 11
    11 - 11

Algo: check if sum of arr is even if not then not possible to get equal sum 
      if sum is even we only need to find half of sum of arr
      apply subset sum 
      
"""


arr = [1,5,11,6]



def equal_sum_partition(arr):
    if sum(arr)%2 != 0:
        return False

    n = len(arr)
    target = sum(arr)//2
    dp = [[0 for i in range(target+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(target+1):
            if i == 0:
                dp[i][j] = False
            elif j == 0:
                dp[i][j] = True
            elif arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]   #(True or False)
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][target]
print(equal_sum_partition(arr))



