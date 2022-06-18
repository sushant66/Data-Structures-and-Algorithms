"""
Find number of LIS
eg: 1 3 5 4 7
	ans = 2
	1 3 4 7
	1 3 5 7

Algo: same as list just use an additional count array (initialize by 1) and whenever 
		lis increase then count[i] = count[j]
		else if 1+dp[j] == dp[i] then count[i]+=count[j]
"""


        
    #1 3 5 4 7 8
#dp  1 2 3 3 4 5
#cnt 1 1 1 1 2 2

n = len(nums)
dp = [1 for i in range(n)]
count = [1 for i in range(n)]
maxi = 1 
for i in range(1,n):
    for j in range(i):
        if nums[i]>nums[j] and dp[i]< 1+dp[j]:
            dp[i] = 1+dp[j]
            count[i] = count[j]
        
        elif nums[i]>nums[j] and dp[i] == 1+dp[j]:
            count[i]+=count[j]
        
    maxi = max(maxi, dp[i])
        
ans = 0
for i in range(n):
    if maxi == dp[i]:
        ans+=count[i]
return ans
        

