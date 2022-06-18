"""
Longest Increasing Subsequence

arr = [10,9,2,5,3,7,101,18]
LIS = 2-5-7-101 or 2-3-7-18
Output = 4

Algo: take not take approach  (max take and not take)
    f(ind, prev) - compare index with previous

"""

nums = [10,9,2,5,3,7,101,18]

#Recursion
def lis(nums,i,prev):
    if i == len(nums):
        return 0

    if prev == -1 or nums[i]>nums[prev]:
        return max(1 + lis(nums,i+1,i), lis(nums,i+1,prev))    #max of take not take
    return lis(nums,i+1,prev)

print(lis(nums,0,-1))

#Memoization
def lis(nums,i,prev,dp):
    if i == len(nums):
        return 0

    if dp[i][prev+1] == -1:
        if prev == -1 or nums[i]>nums[prev]:
            dp[i][prev+1] = max(1 + lis(nums,i+1,i,dp), lis(nums,i+1,prev,dp))    #max of take not take
        else:
            dp[i][prev+1] = lis(nums,i+1,prev,dp)
    return dp[i][prev+1]

n = len(nums)
dp = [[-1 for i in range(n+1)] for j in range(n)]
print(lis(nums,0,-1,dp))

#Tabulation
dp = [[0 for i in range(n+1)] for j in range(n+1)]
for i in range(n-1,-1,-1):
    for j in range(i-1,-2,-1):
        if j == -1 or nums[i]>nums[j]:
            dp[i][j+1] = max(1+dp[i+1][i+1], dp[i+1][j+1])
        else:
            dp[i][j+1] = dp[i+1][j+1]
print(dp[0][0])

#Space optimization
dp = [0 for i in range(n+1)] 
for i in range(n-1,-1,-1):
    temp = [0 for k in range(n+1)] 
    for j in range(i-1,-2,-1):
        if j == -1 or nums[i]>nums[j]:
            temp[j+1] = max(1+dp[i+1], dp[j+1])
        else:
            temp[j+1] = dp[j+1]
    dp = temp
print(dp[0])




# METHOD 2
# each element wil have 1 lis i.e itself
dp = [1 for i in range(n)]
for i in range(n):
    for j in range(0,i):
        if nums[i]>nums[j]:
            dp[i] = max(1+dp[j], dp[i])

print(dp)
print(max(dp))

#Print LIS
has = [i for i in range(n)] 
dp = [1 for i in range(n)]

lastindex = 0
maxi = 0
for i in range(n):
    for j in range(0,i):
        if nums[i]>nums[j] and dp[i] < 1+dp[j]:
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

# METHOD 3 (Binary Search)
import bisect
def lis(arr):
    dp = [arr[0]]
    count = 1
    for i in range(1,len(arr)):
        if arr[i] >dp[-1]:
            dp.append(arr[i])
            count+=1
        else:
            ind = bisect.bisect_left(dp,arr[i])  #lower bound(high in BS)
            dp[ind] = arr[i]
    return count

print(lis(nums))

# Method 4 (Binary search less code)
def lis(nums):
    dp = [10**10] * (len(nums) + 1)
    for elem in nums: dp[bisect_left(dp, elem)] = elem  
    return dp.index(10**10)  #or bisect_left(dp,10**10)
