
"""
You have been given an N*M matrix filled with integer numbers, find the maximum sum that can be obtained from a path starting from any cell in the first row to any cell in the last row.
From a cell in a row, you can move to another cell directly below that row, or diagonally below left or right. So from a particular cell (row, col), we can move in three directions i.e.


eg = arr = [[1, 2, 10, 4],
    [100, 3, 2, 1],
    [1, 1, 20, 2],
    [1, 2, 2, 1]]
ans = 2+100+1+2 = 105
"""

arr = [[1, 2, 10, 4],
    [100, 3, 2, 1],
    [1, 1, 20, 2],
    [1, 2, 2, 1]]

#Recursion
def max_path_sum(arr, i, j):
    if j<0 or j >= len(arr[0]):
        return -float('inf')

    if i == 0:
        return arr[0][j]

    d = arr[i][j] + max_path_sum(arr, i-1, j)
    dg_l = arr[i][j] + max_path_sum(arr, i-1, j-1)
    dg_r = arr[i][j] + max_path_sum(arr, i-1, j+1)
    return max(d,dg_l,dg_r)

n = len(arr)
m = len(arr[0])
max_ = -float('inf')
for k in range(m):
    temp = max_path_sum(arr,n-1,k)
    max_ = max(max_, temp)
print(max_)

# Memoization
def max_path_sum(arr, i, j, dp):
    if j<0 or j >= len(arr[0]):
        return -float('inf')

    if i == 0:
        return arr[0][j]

    if dp[i][j] == -1:
        d = arr[i][j] + max_path_sum(arr, i-1, j, dp)
        dg_l = arr[i][j] + max_path_sum(arr, i-1, j-1,dp)
        dg_r = arr[i][j] + max_path_sum(arr, i-1, j+1, dp)
        dp[i][j] =  max(d,dg_l,dg_r)
    return dp[i][j]

n = len(arr)
m = len(arr[0])
dp = [[-1 for i in range(m)] for j in range(n)]
max_ = -float('inf')
for k in range(m):
    temp = max_path_sum(arr,n-1,k, dp)
    max_ = max(max_, temp)
print(max_)


# Tabulation 
n = len(arr)
m = len(arr[0])
dp = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        dp[0][j] = arr[0][j]


for i in range(1, n):
    for j in range(1, m):
        d = arr[i][j] + dp[i-1][j]
        dg_l = -float('inf')
        dg_r = -float('inf')
        if j < m-1:
            dg_l = arr[i][j] + dp[i-1][j+1]
        if j > 0:
            dg_r = arr[i][j] + dp[i-1][j-1]
        dp[i][j] = max(d,dg_l,dg_r)


for k in range(m):
    max_ = max(max_, dp[n-1][k])
print(max_)


# Space Optimization 
n = len(arr)
m = len(arr[0])
dp = [0 for i in range(m)]
for i in range(n):
    for j in range(m):
        dp[j] = arr[0][j]


for i in range(1, n):
    temp = [0 for i in range(m)]
    for j in range(1, m):
        d = arr[i][j] + dp[j]
        dg_l = -float('inf')
        dg_r = -float('inf')
        if j < m-1:
            dg_l = arr[i][j] + dp[j+1]
        if j > 0:
            dg_r = arr[i][j] + dp[j-1]
        temp[j] = max(d,dg_l,dg_r)
    dp = temp


for k in range(m):
    max_ = max(max_, dp[k])
print(max_)

