
"""
Partition array for max sum

Partition array to get the max sum

eg arr = [1,15,7,9,2,5,10], k = 3
        when you partition replace all element by max in that partition
        arr becomes [15,15,15,9,10,10,10]
        ans = 15*3 + 9 + 10*3 = 84


Algo: Use front partition technique
      start from f(0) and solve for f(i+1)
      loop from j=i to min(i+k,n)
      max_sum = max(max_sum, maxi*l + f(j+1))

"""
arr = [1,15,7,9,2,5,10]
k = 3
n = len(arr)

# Recursion
def partition_max(i):
    if i == n:
        return 0

    l = 0 
    maxi = -float('inf')
    max_ans = -float('inf')

    for j in range(i,min(i+k,n)):
        l+=1
        maxi = max(maxi,arr[j])
        max_ans = max(max_ans, (maxi*l) + partition_max(j+1))

    return max_ans

print(partition_max(0))


# Memoization
def partition_max(i):
    if i == n:
        return 0
    if dp[i] == -1:
        l = 0 
        maxi = -float('inf')
        max_ans = -float('inf')

        for j in range(i,min(i+k,n)):
            l+=1
            maxi = max(maxi,arr[j])
            max_ans = max(max_ans, (maxi*l) + partition_max(j+1))

        dp[i] = max_ans
    return dp[i]

dp = [-1 for i in range(n)]
print(partition_max(0))

# Tabulation
dp = [0 for i in range(n+1)]

for i in range(n-1,-1,-1):
    l = 0
    maxi = -float('inf')
    max_ans = -float('inf')
    for j in range(i,min(i+k,n)):
        l+=1
        maxi = max(maxi,arr[j])
        max_ans = max(max_ans, (maxi*l) + dp[j+1])
    dp[i] = max_ans

print(dp[0])


