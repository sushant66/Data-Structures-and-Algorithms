"""
Edit Distance
Given two strings find min operations(insert/delete/replace) to make a s1 to s2

s1 = "horse"
s2 = "ros"

#delete "e" delete "r" (s1) replace "h"   3 operations

Algo:	
	if match go ahead f(i-1, j-1)
	if not match 1. insert 1+f(i,j-1)   --> hypothetical insert  (horse s) i is still at e
				 2. delete 1+f(i-1,j)   --> i moves to s
				 3. replace 1+f(i-1,j-1)   --> after replace both will be equal hence move ahead
	
	Base case:
		if s1 is exhauseted then we need j insertions to make s2
		eg s1 = "horse"   s2="ros" i=-1 j is at 1 we need 2 insertion ro
		if s2 is exhauseted then we need i deletion to make s2
		eg s1 = "horse" s2 = "" i=1 j = -1 we need 2 deletion ho
		
	
"""

s1 = "horse"
s2 = "ros"

#Recursion

def edit_distance(s1,s2,i,j):
    if j < 0: return i+1
    if i < 0: return j+1

    if s1[i] == s2[j]:
        return edit_distance(s1,s2,i-1,j-1)
    return 1 + min( edit_distance(s1,s2,i,j-1),  
                    edit_distance(s1,s2,i-1,j),  
                    edit_distance(s1,s2,i-1,j-1) )  

print(edit_distance(s1,s2,len(s1)-1,len(s2)-1))


# Memoization
n = len(s1)
m = len(s2)

dp = [[-1 for i in range(m)] for j in range(n)]
def edit_distance(s1,s2,i,j,dp):
    if j < 0: return i+1
    if i < 0: return j+1

    if dp[i][j] == -1:

        if s1[i] == s2[j]:
            dp[i][j] = edit_distance(s1,s2,i-1,j-1,dp)
        else:
            dp[i][j] = 1 + min( edit_distance(s1,s2,i,j-1,dp),  
                        edit_distance(s1,s2,i-1,j,dp),  
                        edit_distance(s1,s2,i-1,j-1,dp) )  
    
    return dp[i][j]

print(edit_distance(s1,s2,len(s1)-1,len(s2)-1, dp))


#Tabulation
dp = [[0 for i in range(m+1)] for j in range(n+1)]
for i in range(n+1):
    for j in range(m+1):
        if i == 0:
            dp[i][j] = j
        if j == 0:
            dp[i][j] = i

for i in range(1, n+1):
    for j in range(1,m+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

print(dp[n][m])


# Space Optimization
dp = [0 for i in range(m+1)] 
for i in range(n+1):
    for j in range(m+1):
        if j == 0:
            dp[j] = i

for i in range(1, n+1):
    temp = [0 for k in range(m+1)] 
    temp[0] = i    # Every time for 0 it will have i
    for j in range(1,m+1):
        if s1[i-1] == s2[j-1]:
            temp[j] = dp[j-1]
        else:
            temp[j] = 1 + min(dp[j], temp[j-1], dp[j-1])
    dp = temp
    
print(dp[m])



