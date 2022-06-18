
"""
 Calculate min path sum to reach from 0,0 to r,c

"""

grid = [
    [5,9,6],
    [11,5,2]
]

#recursion
def min_path_sum(grid, r, c):
    if r == len(grid)-1 and c == len(grid[0])-1:
        return grid[r][c]
    if r >= len(grid) or c >= len(grid[0]):
        return float('inf')

    temp = grid[r][c] + min(min_path_sum(grid, r+1,c), min_path_sum(grid, r, c+1))
    return temp

print(min_path_sum(grid, 0,0))


#memoization
def min_path_sum(grid, r, c, dp):
    if r == len(grid)-1 and c == len(grid[0])-1:
        return grid[r][c]
    if r > len(grid)-1 or c > len(grid[0])-1:
        return float('inf')
    
    if dp[r][c] != -1:
        return dp[r][c]
    dp[r][c] = grid[r][c] + min(min_path_sum(grid, r+1,c,dp), min_path_sum(grid, r, c+1,dp))
    return dp[r][c]

dp = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
print(min_path_sum(grid, 0,0, dp))

#tabulation
dp = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]


for r in range(len(grid)):
    for c in range(len(grid[0])):
        if r == 0 and c == 0:
            dp[r][c] = grid[r][c]
        else:
            x = float('inf')
            y = float('inf')
            if r > 0:
                x = dp[r-1][c]+grid[r][c]
            if c > 0:    
                y = dp[r][c-1]+grid[r][c]
            dp[r][c] = min(x,y)

print(dp[1][2])


#space optimization
"""
Storing previous row in dp and current in temp then dp = temp

"""

dp = [0 for i in range(len(grid[0]))]


for r in range(len(grid)):
    temp = [0 for i in range(len(grid[0]))]
    for c in range(len(grid[0])):
        if r == 0 and c == 0:
            temp[c] = grid[r][c]
        else:
            x = float('inf')
            y = float('inf')
            if r > 0:
                x = dp[c]+grid[r][c]               #previous row
            if c > 0:    
                y = temp[c-1]+grid[r][c]           #previous col
            temp[c] = min(x,y)
    dp = temp
print(dp[2])
