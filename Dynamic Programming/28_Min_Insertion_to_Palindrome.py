"""
Minimum insertion to make a string palindrome
eg = 'abcaa'  - 'abcacba'   ans = 2 added cb

Algo: Keep longest palindromic subsequence intact
eg 'abcaa'     a     a     a                a    c    a
               a  bc a  cb a        or      a ab  c  ba a

So as per this ans = len(s) - lps(s)
"""
s = 'abcaa'
def lps(s):
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

print(len(s)-lps(s))
