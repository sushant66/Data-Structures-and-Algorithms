
"""
    Alice and bob start from 0,0 and 0,c-1 respectively find out max points they can pick after reaching the bottom of matrix
    for overlapping consider just one

    Input: ‘R’ = 3, ‘C’ = 4
       ‘GRID’ = [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]
Output: 21

Initially Alice is at the position (0,0) he can follow the path (0,0) -> (1,1) -> (2,1) and will collect 2 + 4 + 6 = 12 chocolates.

Initially Bob is at the position (0, 3) and he can follow the path (0, 3) -> (1,3) -> (2, 3) and will colllect 2 + 2 + 5 = 9 chocolates.

Hence the total number of chocolates collected will be 12 + 9 = 21. there is no other possible way to collect a greater number of chocolates than 21.


# ALGO: Fixed starting point variable ending point
"""

arr = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
# arr = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]

#Recursion
def cherry_pick(arr,i,j,y):
    if y < 0 or y >= len(arr[0]) or j < 0 or j >= len(arr[0]):          #left right bound
        return -float('inf')
    if i == len(arr)-1:
        if j == y: return arr[i][j]
        return arr[i][j]+arr[i][y]
    
    max_ = -float('inf')
    for k1 in range(-1,2):              #-1,0,1  left,current,right
        for k2 in range(-1,2):
            if j == y:
                temp = arr[i][j] + cherry_pick(arr,i+1,j+k1,y+k2)
            else:
                temp = arr[i][j] + arr[i][y] + cherry_pick(arr,i+1,j+k1,y+k2)
            max_ = max(temp, max_)
    return max_


print(cherry_pick(arr,0,0,len(arr[0])-1))

#Memoization
def cherry_pick(arr,i,j,y, dp):
    if y < 0 or y >= len(arr[0]) or j < 0 or j >= len(arr[0]):          #left right bound
        return -float('inf')
    if i == len(arr)-1:
        if j == y: return arr[i][j]
        return arr[i][j]+arr[i][y]
    
    if dp[i][j][y] == -1:
        max_ = -float('inf')
        for k1 in range(-1,2):              #-1,0,1  left,current,right
            for k2 in range(-1,2):
                if j == y:
                    temp = arr[i][j] + cherry_pick(arr,i+1,j+k1,y+k2, dp)
                else:
                    temp = arr[i][j] + arr[i][y] + cherry_pick(arr,i+1,j+k1,y+k2, dp)
                max_ = max(temp, max_)
                dp[i][j][y] = max_
    return dp[i][j][y]


dp = [[[-1 for i in range(len(arr[0]))] for j in range(len(arr[0])) ] for k in range(len(arr)) ]
print(cherry_pick(arr,0,0,len(arr[0])-1, dp))
    
#Tabulation
dp = [[[0 for i in range(len(arr[0]))] for j in range(len(arr[0])) ] for k in range(len(arr)) ]
r = len(arr)
c = len(arr[0])

dp[0][0][c-1] = grid[0][0] + grid[0][c-1]
for i in range(1, r):
    for j in range(c):
        for k in range(c):
        	if j > i or c-k-1 > i: continue			#bounds
            max_ = -float('inf')
            for k1 in range(-1,2):              #-1,0,1  left,current,right
                for k2 in range(-1,2):
                    temp = -float('inf')
                    if j+k1 < 0 or j+k1 >= c or k+k2 < 0 or k+k2 >= c:
                        continue
                    if j == k:
                        temp = arr[i][j] + dp[i-1][j+k1][k+k2]
                    else:
                        temp = arr[i][j] + arr[i][k] + dp[i-1][j+k1][k+k2]
                    max_ = max(temp, max_)
            dp[i][j][k] = max_

return max([max(dp[r-1][j]) for j in range(c-1)])


#Space Optimization
m = len(grid[0])
n = len(grid)
dp = [[0 for i in range(m)] for j in range(m)]


dp[0][m-1] = grid[0][m-1] + grid[0][0]			#base condition
for i in range(1, n):
    temp = [[0 for x in range(m)] for y in range(m)]
    for j in range(m):
        for k in range(m):
        	if j > i or m-k-1 > i: continue			#bounds for eg if I start from 0,0 i can go to only 1,0 1,1 and not 1,2...
            max_ = -float('inf')
            for k1 in range(-1,2):
                for k2 in range(-1,2):
                    t = -float('inf')
                    if j+k1>=0 and k+k2>= 0 and j+k1 < m and k+k2 < m:
                        if j == k:
                            t = grid[i][j] + dp[j+k1][k+k2]
                        else:
                            t = grid[i][j] + grid[i][k] + dp[j+k1][k+k2] 
                    if t > max_:
                        max_ = t
            temp[j][k] = max_
    dp = temp
return max([max(dp[j]) for j in range(m-1)])			#for 2d dp we take max of dp  so in this case we need to take max of 2d dp
