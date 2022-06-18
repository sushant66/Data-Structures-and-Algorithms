"""
If the array given is 'TRIANGLE' = [[1], [2,3], [3,6,7], [8,9,6,10]] the triangle array will look like:

1
2,3
3,6,7
8,9,6,10

For the given triangle array the minimum sum path would be 1->2->3->8. Hence the answer would be 14.

You can go only down and diagonally right

Top down approach as we dont know the end for eg(n-1,m-1 in case of grid)
Recursion is always top down regardless of whether you start from 0 or n-1

"""

"""
                0,0
            1,0     1,1
        2,0     2,1
    3,0    3,1

"""

# Recursion
arr = [[1], [2,3], [3,6,7], [8,9,6,10]]

def triangle_min_path_sum(arr, i,j):
    if i == len(arr)-1:
        return arr[len(arr)-1][j]

    d = arr[i][j] + triangle_min_path_sum(arr,i+1,j)   #go down
    dg = arr[i][j] + triangle_min_path_sum(arr,i+1,j+1) #go diagonal    
    return min(d,dg)

print(triangle_min_path_sum(arr,0,0))

# Memoization
def triangle_min_path_sum(arr, i,j,dp):
    if i == len(arr)-1:
        return arr[len(arr)-1][j]


    if dp[i][j] == -1:
        d = arr[i][j] + triangle_min_path_sum(arr,i+1,j, dp)   #go down
        dg = arr[i][j] + triangle_min_path_sum(arr,i+1,j+1, dp) #go diagonal   
        dp[i][j] = min(d,dg)

    return dp[i][j]


dp = [[-1 for i in range(len(arr))] for j in range(len(arr))]
print(triangle_min_path_sum(arr,0,0,dp))

#Tabulation
n = len(arr)
dp = [[float('inf') for i in range(n)] for j in range(n)]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i == 0:
            dp[i][j] = arr[i][j]
        else:
            dp[i][j] = arr[i][j] + min(dp[i-1][j], dp[i-1][j-1])

print(min(dp[n-1]))

#Space Optimization
n = len(arr)
dp = [float('inf') for i in range(n)]
for i in range(len(arr)):
    temp = [float('inf') for i in range(n)]
    for j in range(len(arr[i])):
        if i == 0:
            temp[j] = arr[i][j]
        else:
            temp[j] = arr[i][j] + min(dp[j], dp[j-1])
    dp = temp
print(min(dp))




