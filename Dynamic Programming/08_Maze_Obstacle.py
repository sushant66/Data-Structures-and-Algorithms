
"""
Count unique path to reach bottom right of grid from top left in a maze with obstacles

"""

grid = [
    [0,0,0],
    [0,-1,0],
    [0,0,0]
]

#recursion
def count_path(grid, r, c):
    if r == len(grid)-1 and c == len(grid[0])-1:
        return 1
    if r >= len(grid) or c >= len(grid[0]) or grid[r][c] == -1:
        return 0
    
    x = count_path(grid, r+1,c)
    y = count_path(grid, r, c+1)

    return x+y

print(count_path(grid, 0,0))


#memoization
def count_path(grid, r, c, dp):
    if r == len(grid)-1 and c == len(grid[0])-1:
        return 1
    if r > len(grid)-1 or c > len(grid[0])-1 or grid[r][c] == -1:
        return 0
    
    if dp[r][c] != -1:
        return dp[r][c]
    x = count_path(grid, r+1,c, dp)
    y = count_path(grid, r, c+1, dp)
    dp[r][c] = x+y
    return x+y

dp = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
print(count_path(grid, 0,0, dp))

#tabulation
dp = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]


for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == -1:
            dp[r][c] = 0
        elif r == 0 and c == 0:
            dp[r][c] = 1
        else:
            x = 0
            y = 0
            if r > 0:
                x = dp[r-1][c]
            if c > 0:    
                y = dp[r][c-1]
            dp[r][c] = x+y

print(dp[2][2])


#space optimization
"""
Storing previous row in dp and current in temp then dp = temp

"""

dp = [0 for i in range(len(grid[0]))]


for r in range(len(grid)):
    temp = [0 for i in range(len(grid[0]))]
    for c in range(len(grid[0])):
        if grid[r][c] == -1:
            temp[c] = 0
        elif r == 0 and c == 0:
            temp[c] = 1
        else:
            x = 0
            y = 0
            if r > 0:
                x = dp[c]               #previous row
            if c > 0:    
                y = temp[c-1]           #previous col
            temp[c] = x+y
    dp = temp
print(dp[2])
