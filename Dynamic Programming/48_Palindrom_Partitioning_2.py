"""
Palindrome Partitioning II

Partition palindrome in minimum cuts
eg aab - cut in aa and b so ans = 1


Algo: front partition method
        precompute the palindromes using extendpalindrome method add all r in d[l] dict of set
        start from 0 and then it will check from i to n
        if i to j is palindrome (j in d[i]) solve from j+1 to n take min value
        subtract 1 from answer as recursion will partition at end also
"""


s = "abababc"


def check_palindrome(l,r):
    if l>=r: return True
    if s[l] != s[r]: return False
    return check_palindrome(l+1,r-1)

# Recursion
def min_partition(i):
    if i == len(s):
        return 0

    mini = float('inf')
    for j in range(i,len(s)):
        if check_palindrome(i,j):
            mini = min(mini, 1+min_partition(j+1))
            # print(mini)
        
    return mini
print(min_partition(0)-1)   #-1 because recursion does partition at end
        

#Memoization
def min_partition(i,dp):
    if i == len(s):
        return 0

    if dp[i] == -1:
        mini = float('inf')
        for j in range(i,len(s)):
            if check_palindrome(i,j):
                mini = min(mini, 1+min_partition(j+1,dp))
                # print(mini)
            
        dp[i] = mini
    return dp[i]

n = len(s)
dp = [-1 for i in range(n)]
print(min_partition(0,dp)-1)   


#Tabulation
dp = [0 for i in range(n+1)]
for i in range(n-1,-1,-1):
    mini = float('inf')
    for j in range(i, n):
        if check_palindrome(i,j):
            mini = min(mini, 1+dp[j+1])
    dp[i] = mini
print(dp[0]-1)
        
    
# Method 2
from collections import defaultdict
d = defaultdict(set)
def extend_palindrome(l,r):
    while l>=0 and r <n and s[l] == s[r]:
        d[l].add(r)
        l-=1
        r+=1

for i in range(len(s)):
    extend_palindrome(i,i)
    extend_palindrome(i,i+1)

dp = [0 for i in range(n+1)]
for i in range(n-1,-1,-1):
    mini = float('inf')
    for j in range(i, n):
        if j in d[i]:
            mini = min(mini, 1+dp[j+1])
    dp[i] = mini
print(dp[0]-1)

