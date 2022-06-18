"""
Wildcard Matching

Check if p can be used to match s
eg:
    s = "abcd"                  s = "abcd"      True            
    p = "abc*"      True        p = "a*d"
    
    s = "abcd"      True        s = "abcd"      True
    p = "ab?d"                  p = "**abcd"
    

Algo:
    if both i<0 and j<0 return True
    if p is remaining then check if all are * then True
    
    if p is * then f(i-1,j) or f(i,j-1) i.e stay at * and move ahead or move ahead from *
    if p is ? or s and p match f(i-1,j-1) move ahead
    at last return false

    ab | ab*
a|ab*       ab|ab   False or True
"""


s = "abcd"
p = "abc*"
# p = "ab?d"
# p = "**abcd"

#Recursion
def wildcard_matching(s,p,i,j):
    if i<0 and j<0: return True
    
    if i < 0:
        for k in range(j+1):
            if p[k] != "*":
                return False
        return True
    
    if j < 0:
        return False    
    
    if s[i] == p[j] or p[j] == '?':
        return wildcard_matching(s,p,i-1,j-1)
    
    
    if p[j] == '*':
        return wildcard_matching(s,p,i,j-1) or wildcard_matching(s,p,i-1,j)
    
    
    return False

print(wildcard_matching(s,p,len(s)-1,len(p)-1))
   
#Memoization
def wildcard_matching(s,p,i,j,dp):
    if i<0 and j<0: return True
    
    if i < 0:
        for k in range(j+1):
            if p[k] != "*":
                return False
        return True
    
    if j < 0:
        return False    
    
    if dp[i][j] == -1:
        if s[i] == p[j] or p[j] == '?':
            dp[i][j] = wildcard_matching(s,p,i-1,j-1,dp)
        
        
        elif p[j] == '*':
            dp[i][j] = wildcard_matching(s,p,i,j-1,dp) or wildcard_matching(s,p,i-1,j,dp)
        else:
            dp[i][j] = False
        
    return dp[i][j]

n = len(s)
m = len(p)        
dp = [[-1 for i in range(m)] for j in range(n)]
print(wildcard_matching(s,p,len(s)-1,len(p)-1,dp))   

 
# Tabulation 
n = len(s)
m = len(p)
dp = [[False for i in range(m+1)] for j in range(n+1)]

dp[0][0] = True                
for i in range(1,n+1):
    dp[i][0] = False

for j in range(1,m+1):
    flag = True
    for i in range(1,j+1):
        if p[i-1] != "*":
            flag = False
            break
    dp[0][j] = flag

for i in range(1,n+1):
    for j in range(1,m+1):
        if p[j-1] == '*':
            dp[i][j] = dp[i-1][j] or dp[i][j-1]
        elif s[i-1] == p[j-1] or p[j-1] == '?':
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = False
print(dp[n][m])

#Space Optimization
dp = [False for i in range(m+1)] 

dp[0] = True                

for j in range(1,m+1):
    flag = True
    for i in range(1,j+1):
        if p[i-1] != "*":
            flag = False
            break
    dp[j] = flag

for i in range(1,n+1):
    temp = [False for k in range(m+1)] 
    for j in range(1,m+1):
        if p[j-1] == '*':
            temp[j] = dp[j] or temp[j-1]
        elif s[i-1] == p[j-1] or p[j-1] == '?':
            temp[j] = dp[j-1]
        else:
            temp[j] = False
    dp = temp
print(dp[m])
