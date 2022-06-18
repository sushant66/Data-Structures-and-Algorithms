"""
	Given height list find min cost to jump to nth stair
	
	cost is height[i-1] - height[j-1]
	eg: [10,20,30,10] ans = 20
	abs(10-20) = 10
	abs(20-10) = 10
	
"""


def frog_jump(cost, n):
    if n == 0: return 0
    if n == 1: return abs(cost[1]-cost[0])

    x = frog_jump(cost, n-1) + abs(cost[n]-cost[n-1])
    y = frog_jump(cost, n-2)+ abs(cost[n]-cost[n-2])
    return min(x, y)

# cost = [10,20,30,10]
cost = [7,4,4,2,6,6,3,4]
print(frog_jump(cost,len(cost)-1))


###  Memoization (Top Down)

def frog_jump(cost, n, dp):
    if n == 0: return 0
    if n == 1: return abs(cost[1]-cost[0])

    if dp[n] == -1:
        x = frog_jump(cost, n-1, dp) + abs(cost[n]-cost[n-1])
        y = frog_jump(cost, n-2, dp) + abs(cost[n]-cost[n-2])
        dp[n] = min(x,y)
    return dp[n]
cost = [7,4,4,2,6,6,3,4]
dp = [-1 for i in range(len(cost))]
print(frog_jump(cost,len(cost)-1, dp))


### Tabulation (Bottom Up)
dp = [-1 for i in range(len(cost))]
n = len(cost)
dp[0] = 0
dp[1] = abs(cost[1]-cost[0])

for i in range(2,n):
    dp[i] = min(dp[i-1]+abs(cost[i]-cost[i-1]), dp[i-2]+abs(cost[i]-cost[i-2]))

print(dp[n-1])



### Space Optimization
dp = [-1 for i in range(len(cost))]
n = len(cost)
first = 0
second = abs(cost[1]-cost[0])
ans = 0
for i in range(2,n):
    ans = min(second+abs(cost[i]-cost[i-1]), first+abs(cost[i]-cost[i-2]))
    first = second
    second = ans

print(ans)


"""
	K jumps
"""


def frog_jump(cost, n, k):
    if n == 0: return 0
    if n == 1: return abs(cost[1]-cost[0])
    ans = float('inf')
    for i in range(1,k+1):
        if n-i >= 0:
            x = frog_jump(cost, n-i,k) + abs(cost[n-i]-cost[n])
            ans = min(x, ans)
    return ans

# cost = [10,20,30,10]
cost = [7,4,4,2,6,6,3,4]
print(frog_jump(cost,len(cost)-1,3))


# Memoization
def frog_jump(cost, n, k, dp):
    if n == 0: return 0
    if n == 1: return abs(cost[1]-cost[0])
    ans = float('inf')
    if dp[n] == -1:
        for i in range(1,k+1):
            if n-i >= 0:
                x = frog_jump(cost, n-i,k, dp) + abs(cost[n-i]-cost[n])
                ans = min(x, ans)
                dp[n] = ans
    return dp[n]

cost = [7,4,4,2,6,6,3,4]
dp = [-1 for i in range(len(cost))]
print(frog_jump(cost,len(cost)-1,3, dp))


#Tabulation
cost = [7,4,4,2,6,6,3,4]
dp = [0 for i in range(len(cost))]
n =len(cost)
k=3
dp[0] = 0
for i in range(1, n):
    ans = float('inf')
    for j in range(1,k+1):
        if (i-j)>=0:
            x = dp[i-j]+abs(cost[i]-cost[i-j])
            ans = min(x, ans)
    dp[i] = ans
print(dp[n-1])
