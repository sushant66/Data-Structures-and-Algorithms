"""
Distinc Subsequnces 
String Matching
s1 = "babgbag"
s2 = "bag"
Count how many times we can match string s2 with s1

"""


s1 = "babgbag"
s2 = "bag"


#Recursion
def distinct_subsequences(s1,s2,i,j):
    if j < 0:
        return 1
    if i < 0:
        return 0
    
    if s1[i-1] == s2[j-1]:
        return distinct_subsequences(s1,s2,i-1,j-1) + distinct_subsequences(s1,s2,i-1,j)
 
    return distinct_subsequences(s1,s2,i-1,j)
        
print(distinct_subsequences(s1,s2,len(s1)-1,len(s2)-1))

#Memoization
def distinct_subsequences(s1,s2,i,j, dp):
    if j < 0:
        return 1
        
    if i < 0:
        return 0

    if dp[i][j] == -1:
        if s1[i] == s2[j]:
            dp[i][j] = distinct_subsequences(s1,s2,i-1,j-1, dp) + distinct_subsequences(s1,s2,i-1,j, dp)
        else:
            dp[i][j] = distinct_subsequences(s1,s2,i-1,j, dp)
    return dp[i][j]
        
dp = [[-1 for i in range(len(s2))] for j in range(len(s1))]
print(distinct_subsequences(s1,s2,len(s1)-1,len(s2)-1, dp))

# Tabulation
n = len(s1)
m = len(s2)
dp = [[0 for i in range(m+1)] for j in range(n+1)]

for i in range(n+1):
    for j in range(m+1):
        if i == 0:
            dp[i][j] = 0
        if j == 0:
            dp[i][j] = 1
        elif s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]
            
print(dp[n][m])
    
# Space Optimization
n = len(s1)
m = len(s2)
dp = [0 for i in range(m+1)]
dp[0] = 1
for i in range(n+1):
    temp = [0 for k in range(m+1)]
    for j in range(m+1):
        if i == 0:
            temp[j] = 0
        if j == 0:
            temp[j] = 1
        elif s1[i-1] == s2[j-1]:
            temp[j] = dp[j-1] + dp[j]
        else:
            temp[j] = dp[j]
    dp = temp
print(dp[m])
    
