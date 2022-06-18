"""
Burst baloons

Burst baloons to get max coins
if you burst ith balon you ll get a[i-1] +a[i] +a[i+1] coins if no one on left or right 
    multiply by 1

eg [3,1,5,8]
coints =  3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 167



Algo: Move in opposite direction (from last bursted ballon to up)
    eg 8 is the last guy then it will be 1*8*1 then move up 
    lets say 5 then 1*5*8    
    steps = a[i-1]*a[k]*a[j+1] + f(i,k-1) + f(k+1,j)
"""
arr = [3,1,5,8]
c = len(arr)
arr.append(1)
arr.insert(0,1)

#Recursion
def burst_baloons(i,j):
    if i>j:
        return 0
    
    maxi = -float('inf')
    for k in range(i,j+1):
        steps = (arr[i-1]*arr[k]*arr[j+1]) + burst_baloons(i,k-1) + burst_baloons(k+1,j)
        maxi = max(steps, maxi)

    return maxi

print(burst_baloons(1,c))

#Memoization
def burst_baloons(i,j,dp):
    if i>j:
        return 0
    if dp[i][j] == -1:
        maxi = -float('inf')
        for k in range(i,j+1):
            steps = (arr[i-1]*arr[k]*arr[j+1]) + burst_baloons(i,k-1,dp) + burst_baloons(k+1,j,dp)
            maxi = max(steps, maxi)

        dp[i][j] = maxi
    return dp[i][j]

dp = [[-1 for i in range(c+2)] for j in range(c+2)]
print(burst_baloons(1,c,dp))

#Tabulation
dp = [[0 for i in range(c+2)] for j in range(c+2)]

for i in range(c,0,-1):
    for j in range(i,c+1):
        maxi = -float('inf')
        for k in range(i,j+1):
            steps = (arr[i-1]*arr[k]*arr[j+1]) + dp[i][k-1] + dp[k+1][j]
            maxi = max(steps, maxi)
        dp[i][j] = maxi
print(dp[1][c])
