"""
	Find min cost to climb nth stair (start from 0 or 1) (take 1 step or 2)
	eg 10,15,20
	ans - 15		start from 1
"""



# cost = [10,15,20]
cost = [1,100,1,1,1,100,1,1,100,1]

"""
          10 15 20
        20+15     20+10
    15+10
"""


def min_cost_climb(cost, n):
    if n == 0: return cost[0]
    if n == 1: return cost[1]

    return min(min_cost_climb(cost, n-1), min_cost_climb(cost, n-2))+cost[n]
       
print(min(min_cost_climb(cost, len(cost)-1), min_cost_climb(cost, len(cost)-2)))


def min_cost_climb(cost, n, dp):
    if n == 0: return cost[0]
    if n == 1: return cost[1]

    if dp[n][cost[n]] == -1:
        dp[n][cost[n]] = min(min_cost_climb(cost, n-1,dp), min_cost_climb(cost, n-2,dp))+cost[n]
    
    return dp[n][cost[n]]
       
dp = [[-1 for i in range(sum(cost)+1)] for j in range(len(cost)+1)]
print(min(min_cost_climb(cost, len(cost)-1, dp), min_cost_climb(cost, len(cost)-2, dp)))


dp = [[0 for i in range(sum(cost)+1)] for j in range(len(cost)+1)]

for i in range(len(cost)):
    for j in range(sum(cost)+1):
        if i == 0:
            dp[i][j] = cost[0]
        elif i == 1:
            dp[i][j] = cost[1]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-2][j])+cost[i]
print(min(dp[len(cost)-1][sum(cost)], dp[len(cost)-2][sum(cost)]))
