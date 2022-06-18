"""
Largest Divisible Subset

eg: nums = [1,16,7,8,4]
	ans = 1,16,8,4             ans[i]%ans[j] == 0 or ans[j]%ans[i] == 0
	
	
Algo: Sort the array as if 8 is divisble by 1 and 16 is divisible by 8 then it has to be divisible by 1 also
	Same as lis just replace > with % (nums[i]%nums[j] == 0) 
	Use lis printing method to print

"""



nums = [1,16,7,8,4]
nums = [1,2,3]
n = len(nums)


nums.sort()
print(nums)
has = [i for i in range(n)] 
dp = [1 for i in range(n)]

lastindex = 0
maxi = 0
for i in range(n):
    for j in range(0,i):
        if nums[i]%nums[j]==0 and dp[i] < 1+dp[j]:
            has[i] = j
            dp[i] = max(1+dp[j], dp[i])
    
    if dp[i] > maxi:
        maxi = max(dp[i], maxi)
        lastindex = i

print(dp)
print(has)
print(maxi)
print(lastindex)

ans = []
while has[lastindex]!=lastindex:
    ans.append(nums[lastindex])
    lastindex = has[lastindex]
    
ans.append(nums[lastindex])
print(ans[::-1])
