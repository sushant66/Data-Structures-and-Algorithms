"""
Count Square Submatrices with All Ones

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Algo: if matrix[i][j] == 1:
      	dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1], dp[i-1][j-1])
      	
      return sum of all ones in dp

"""

matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

n = len(matrix)
m = len(matrix[0])
dp = [[0 for i in range(m)] for j in range(n)]


for i in range(n):
    dp[i][0] = matrix[i][0]
    
for j in range(m):
    dp[0][j] = matrix[0][j]
    
    

for i in range(1,n):
    for j in range(1,m):
        if matrix[i][j] == 1:
            dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1], dp[i-1][j-1])
    
    
print(sum([sum(i) for i in dp]))
