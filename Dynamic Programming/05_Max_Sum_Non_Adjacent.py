# Recursive 
""""
	Find max sum of subsequence with non adjacent elements
	2 1 4 9 -- 11  (2+9)
	
""""


arr = [1, 2, 3, 1, 3, 5, 8, 1, 9]

def max_sum_non_adjacent(arr,ind):
    if ind == 0:
        return arr[ind]
    if ind < 0:
        return 0

    return max(arr[ind]+ max_sum_non_adjacent(arr,ind-2), max_sum_non_adjacent(arr,ind-1))

print(max_sum_non_adjacent(arr,len(arr)-1))


# Memoization
dp = [-1 for i in range(len(arr))]
def max_sum_non_adjacent(arr,ind, dp):
    if ind == 0:
        return arr[ind]
    if ind < 0:
        return 0

    if dp[ind] == -1:
        dp[ind] = max(arr[ind]+ max_sum_non_adjacent(arr,ind-2, dp), max_sum_non_adjacent(arr,ind-1, dp))
    return dp[ind]

print(max_sum_non_adjacent(arr,len(arr)-1, dp))


# Tabulation

dp = [-1 for i in range(len(arr))]
dp[0] = arr[0]

for i in range(1, len(arr)):
    if i>1:
        dp[i] = max(arr[i]+dp[i-2], dp[i-1])
    else:    
        dp[i] = max(arr[i], dp[i-1])

print(dp[len(arr)-1])

# Space Optimization

prev1 = arr[0]
prev2 = 0
ans = 0
for i in range(1, len(arr)):
    if i>1:
        ans = max(arr[i]+prev2, prev1)
    else:    
        ans = max(arr[i], prev1)
    prev2 = prev1
    prev1 = ans

print(ans)



""""
	House Robber
	Non adjacent max sum if array is circular
""""

arr = [2,3,2]   # ans = 3
def max_sum_non_adjacent(arr):
	prev1 = arr[0]
	prev2 = 0
	ans = 0
	for i in range(1, len(arr)):
		if i>1:
		    ans = max(arr[i]+prev2, prev1)
		else:    
		    ans = max(arr[i], prev1)
		prev2 = prev1
		prev1 = ans

	return ans
print(max(max_sum_non_adjacent(arr[1:]), max_sum_non_adjacent(arr[:-1])) )


