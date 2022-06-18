"""
You are given an array containing N non-negative integers. Your task is to partition this array into two subsets such that the absolute difference between subset sums is minimum.
You just need to find the minimum absolute difference considering any valid division of the array elements.

ALgo : using subset sum with target of total sum and then find a subset sum with min diff

"""
#Tabulation
# arr = [3,9,7,3]
arr = [8,6,5]
k = sum(arr)

def min_subset_sum_diff(arr,k):
    n = len(arr)
    dp = [[False for i in range(k+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(k+1):
            if i == 0:
                dp[i][j] = False
            if j == 0:
                dp[i][j] = True
            elif arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]   #(True or False)
            else:
                dp[i][j] = dp[i-1][j]
    
    mini = float('inf')
    for i in range(k):
        if dp[n][i] == True:
            s1 = i
            s2 = k-i
            mini = min(mini, abs(s2-s1))
    return mini

print(min_subset_sum_diff(arr,k))


#Space Optimization
arr = [8,6,5]
k = sum(arr)

def min_subset_sum_diff(arr,k):
    n = len(arr)
    dp = [False for i in range(k+1)] 
    for i in range(n+1):
        temp = [0 for i in range(k+1)] 
        for j in range(k+1):
            if i == 0:
                temp[j] = False
            if j == 0:
                temp[j] = True
            elif arr[i-1] <= j:
                temp[j] = dp[j-arr[i-1]] or dp[j]   #(True or False)
            else:
                temp[j] = dp[j]
        dp = temp
    mini = float('inf')
    for i in range(k):
        if dp[i] == True:
            s1 = i
            s2 = k-i
            mini = min(mini, abs(s2-s1))
    return mini
print(min_subset_sum_diff(arr,k))

