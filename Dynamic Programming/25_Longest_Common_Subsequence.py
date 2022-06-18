"""

Longest Common subsequence
a1 = "fcabd"
a2 = "xacbd"
here lcs is abd or cbd i.e len 3

"""

a1 = "fcabd"
a2 = "xacbd"

a1 = "mhunuzqrkzsnidwbun"
a2 = "szulspmhwpazoxijwbq"

a1 = "bsbininm"
a2 = "jmjkbkjkv"


#Recursion
def lcs(a1,a2,i,j):
    if i < 0 or j < 0:
        return 0


    if a1[i] == a2[j]:
        return 1 + lcs(a1,a2,i-1,j-1)
    return max(lcs(a1,a2,i-1,j), lcs(a1,a2,i,j-1))

print(lcs(a1,a2,len(a1)-1,len(a2)-1))

#Memoization
dp = [[-1 for i in range(len(a2))] for j in range(len(a1))]
def lcs(a1,a2,i,j,dp):

    if i < 0 or j < 0:
        return 0
    
    if dp[i][j] == -1:
        if a1[i] == a2[j]:
            return 1 + lcs(a1,a2,i-1,j-1,dp)
        dp[i][j] = max(lcs(a1,a2,i-1,j,dp), lcs(a1,a2,i,j-1,dp))
    return dp[i][j]

print(lcs(a1,a2,len(a1)-1,len(a2)-1,dp))

#Tabulation
# we use shifting of index as for i = 0 and j == 0 python will start from back j-1 = -1
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
    temp = [0 for x in range(n+1)]
    for j in range(n+1):
        if i==0 or j == 0:
            temp[j] = 0
        elif a1[i-1] == a2[j-1]:
            temp[j] = 1 + dp[j-1]
        else:
            temp[j] = max(dp[j],temp[j-1])
    dp = temp

print(dp[n])


#Print LCS (Only one)
i = m
j = n
res = ''
while i >0 and j >0:
    if a1[i-1] == a2[j-1]:
        res+=a1[i-1]
        i-=1
        j-=1
    elif dp[i-1][j] > dp[i][j-1]:
        i-=1
    else:
        j-=1
print(res[::-1])


#Print all LCS
#Run after LCS Tabulation
def lcs_print_all(a1,a2,i,j):
    s = set()
    if i == 0 or j == 0:
        s.add('')
        return s
    
    if a1[i-1] == a2[j-1]:
        temp = lcs_print_all(a1,a2,i-1,j-1)
        for t in temp:
            s.add(t+a1[i-1])
    else:
        if dp[i-1][j] >= dp[i][j-1]:
            s = lcs_print_all(a1,a2,i-1,j)
        if dp[i][j-1] >= dp[i-1][j]:
            temp = lcs_print_all(a1,a2,i,j-1)
            for t in temp:              #same as l+r
                s.add(t)
    return s
print(lcs_print_all(a1,a2,len(a1),len(a2)))
