
"""
Find longest common substring in two strings
eg abdz, abxd
ans = ab i.e len = 2
Algo: Same as Longest Common Subsequence just we dont skip(max(dp[i][j-1],dp[i-1][j])) instead set dp[i][j] = 0
At last take max from the dp array
"""


# a1 = "fcabd"
# a2 = "xacbd"

a1 = "mhunuzqrkzsnidwbun"
a2 = "szulspmhwpazoxijwbq"

# a1 = "xy"
# a2 = "ay"

# a1 = "bsbininm"
# a2 = "jmjkbkjkv"


#Recursion
def lcsubstring(s1,s2,i,j, res):
    if i < 0 or j < 0:
        return res
    
    
    if s1[i] == s2[j]:
        return lcsubstring(s1,s2,i-1,j-1, res+1)
    return max(res, lcsubstring(s1,s2,i,j-1,0), lcsubstring(s1,s2,i-1,j,0)) 

print(lcsubstring(s1,s2,len(s1)-1,len(s2)-1,0))


#Tabulation
#We stop at -1 thats why we use shifting of index
m = len(a1)
n = len(a2)
dp = [[0 for i in range(n+1)] for j in range(m+1)]
ans = -float('inf')
for i in range(m+1):
    for j in range(n+1):
        if i == 0 or j == 0:                
            dp[i][j] = 0  
        elif a1[i-1] == a2[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
            ans = max(dp[i][j], ans)
        else:
            dp[i][j] = 0

print(ans)

#Space Optimization
m = len(a1)
n = len(a2)
dp = [0 for i in range(n+1)] 
ans = -float('inf')
for i in range(m+1):
    temp = [0 for i in range(n+1)] 
    for j in range(n+1):
        if i == 0 or j == 0:                
            temp[j] = 0  
        elif a1[i-1] == a2[j-1]:
            temp[j] = 1 + dp[j-1]
            ans = max(temp[j], ans)
        else:
            temp[j] = 0
    dp = temp

print(ans)


#Print 
n = len(s)
m  = len(x)
dp = [[0 for i in range(m+1)] for j in range(n+1)]
ans = -float('inf')
row = 0
col = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if s[i-1] == x[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
            if dp[i][j] > ans:
                ans = dp[i][j]
                row = i
                col = j
        else:
            dp[i][j] = 0
print(ans)
res = ''
while dp[row][col] != 0:
    res += s[row-1]
    row-=1
    col-=1

print(res[::-1])
