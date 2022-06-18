"""
Partition DP

Whenever there is multiple pattern which can be solved by diff ways use partition dp
eg: A B C matrix multiplication
	so (A*B)*C (A)*(B*C) ... So there can be many such ways

Matrix Chain Multiplication 
Find the min operation need for matrix multiplication
eg 3 matrix  10x30 30x5 5x60                    if we take A*(BC)
		A*B = 10*30*5 = 1500					B*C = 30*5*60 = 9000
		AB will give 10x5 matrix                BC will give 30x60 matrix
		(AB)*C = 10*5*60 = 3000                 A*(BC) = 10*30*60 = 18000
		Total = 3000+1500 = 4500                Total = 9000+18000 = 27000
		So min is 4500

Input: [10,20,30,40,50]  -- A = 10x20 B = 20x30 ....
		A[i] = A[i]*A[i-1]


Partition DP Rules:
	Start with entire block/array f(i,j) i-start j-end
	Try all partition -- Run a loop to try all partition
	Return best possible 2 partition

"""


arr = [10,20,30,40,50]

n = len(arr)

#Recursion
def mcm(i,j):
    if i == j:      #only 1 matrix left
        return 0 

    mini = float('inf')
    for k in range(i,j):   #j-1 for bcd * e so if we cover e also there will be no one on right
        steps = (arr[i-1]*arr[k]*arr[j]) + mcm(i,k) + mcm(k+1,j)    #eg AB*CD -- 10x20  20x30 - 10x30  30x40 40x50 - 30x50 - 10x30x50
        mini = min(mini, steps)

    return mini

print(mcm(1,n-1))
#start from 1 because A[i] = A[i-1]*A[i]

#Memoization
def mcm(i,j,dp):
    if i == j:      
        return 0 

    if dp[i][j] == -1:

        mini = float('inf')
        for k in range(i,j):   
            steps = (arr[i-1]*arr[k]*arr[j]) + mcm(i,k,dp) + mcm(k+1,j,dp)    
            mini = min(mini, steps)

        dp[i][j] = mini
    return dp[i][j]

dp = [[-1 for i in range(n)] for j in range(n)]
print(mcm(1,n-1,dp))

#Tabulation
dp = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    dp[i][i] = 0

for i in range(n-1,0,-1):
    for j in range(i+1,n):
        mini = float('inf')
        for k in range(i,j):
            steps = (arr[i-1]*arr[k]*arr[j]) + dp[i][k] + dp[k+1][j]
            mini = min(steps,mini)
        dp[i][j] = mini
print(dp[1][n-1])
