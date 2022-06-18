"""
Longest Bitonic Subsequence

Bitonic means moutain array (it can be complete increasing/decreasing or increasing+decreasing)

nums = [2,1,1,5,6,2,3,1]
longest = 1,5,6,3,1 
Output = 5

Algo:  Same as lis
	   calculate lis of nums and reverse of nums 
	   take max 
	   maxi = max(maxi, dp1[i]+dp2[i]-1)   (max lis from left max lis from right till i and i will be common hence -1)
	   

"""



def lis(nums):
    dp = [1 for i in range(len(nums))]
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i]>nums[j] and 1+dp[j]>dp[i]:
                dp[i] = 1+dp[j]
        
    return dp

max_bitonic = 
dp1 = lis(nums)
dp2 = lis(nums[::-1])[::-1]					#we need to compare from start hence reverse list and then again reverse to be on same page

for i in range(len(nums)):
    max_bitonic = max(max_bitonic, dp1[i]+dp2[i]-1)

print(max_bitonic)



#Method 2
def lis(nums):
    dp = [float('inf')] * (len(nums) + 1)
    lens = [0]*len(nums)
    for i, elem in enumerate(nums): 
        lens[i] = bisect_left(dp, elem) + 1
        dp[lens[i] - 1] = elem 
    return lens

l1, l2 = lis(nums), lis(nums[::-1])[::-1]

ans = 0 
n = len(nums)
for i in range(n):
    if l1[i]>1 and l2[i]>1:
        ans = max(ans, l1[i]+l2[i]-1)
    
print(ans)
