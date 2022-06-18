"""
Find longest palindromic subsequence

eg: “bbabcbcab”       ans = “babcbab”  len = 7

Algo: Same as LCS      use LCS(s,s[::-1])

So LCS of string and its reverse will give us the longest palindromic subsequence
"""



a1 = "bbabcbcab"
a2 = a1[::-1]
#Tabulation
#We stop at -1 thats why we use shifting of index
m = len(a1)
n = len(a2)
dp = [[0 for i in range(n+1)] for j in range(m+1)]

for i in range(m+1):
    for j in range(n+1):
        if i == 0 or j == 0:                
            dp[i][j] = 0  
        elif a1[i-1] == a2[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[m][n])

#Space Optimization
m = len(a1)
n = len(a2)
dp = [0 for i in range(n+1)] 
for i in range(m+1):
    temp = [0 for i in range(n+1)] 
    for j in range(n+1):
        if i == 0 or j == 0:                
            temp[j] = 0  
        elif a1[i-1] == a2[j-1]:
            temp[j] = 1 + dp[j-1]
        else:
            temp[j] = max(dp[j], temp[j-1])
    dp = temp

print(dp[n])



#Efficient Solution
#Recursion
def f(s,l,r):
    if l > r:
        return 0
    if l == r:				#base case when only 1 character is there
        return 1
    
    if s[l] == s[r]:
        return 2 + f(s,l+1,r-1)			# as we are going only half way if we go full way then keep 1
    else:
        return max(f(s,l+1,r), f(s,l,r-1))
return f(s,0,len(s)-1)

#Tabulation
n = len(s)
dp = [[0 for i in range(n)] for j in range(n)]


for l in range(n-1,-1,-1):
    dp[l][l] = 1
    for r in range(l+1,n):      
        if s[l] == s[r]:
            dp[l][r] = 2 + dp[l+1][r-1]
        else:
            dp[l][r] = max(dp[l+1][r], dp[l][r-1])

return dp[0][n-1]

#Space Optimization
n = len(s)
dp = [0 for i in range(n)] 


for l in range(n-1,-1,-1):
    temp = [0 for i in range(n)] 
    temp[l] = 1
    for r in range(l+1,n):      
        if s[l] == s[r]:
            temp[r] = 2 + dp[r-1]
        else:
            temp[r] = max(dp[r], temp[r-1])
    dp = temp
return dp[n-1]
