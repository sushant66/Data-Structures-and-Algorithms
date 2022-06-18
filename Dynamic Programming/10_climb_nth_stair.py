"""
no of possible ways to climb nth stair 
Two choice take 1 step or 2 step
n = 4    5
n = 5    8
"""

def climb_stairs(n, dp):
    if n == 0:
        return 1
    if n < 0 :
        return 0

    if dp[n]!=-1:
        return dp[n]
    
    dp[n] = climb_stairs(n-2, dp) + climb_stairs(n-1, dp) 
    return dp[n]


n = 4
dp = [-1 for i in range(n+1)]
print(climb_stairs(n, dp))
n = 5
dp = [-1 for i in range(n+1)]
print(climb_stairs(n, dp))



##  Same as Fibanacci 
