"""
Min cost to cut stick

Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.
You should perform the cuts in order, you can change the order of the cuts as you wish.
cost of one cut is length of that cut
Return the minimum total cost of the cuts.

eg nums = [1,3,4,5]
    7 + 4 + 3 + 2 = 16  1st cut on len 7 second on len 4 .....

Algo: Use MCM approach 
        sort the array because if we dont sort we can solve them seperately
        eg 1 5 4 3 so 1 and 5 can be solved seperately as it depends on 3 and 4
        steps = cuts[j+1]-cuts[i-1] + f(i,k-1)+f(k+1,i)
"""


n = 7  #length of stick

cuts = [1,3,4,5]
c = len(cuts)
cuts.sort()

cuts.append(n)
cuts.insert(0,0)        #calculate length of stick at that point so at end we have n at start we have 0
print(cuts)             #eg 012|3|456   if we make cut at 3 3-0 = 3 (including 3) 7-3 = 4  (3456)

#Recursion
def min_cost_cut_stick(i,j):
    if i > j:
        return 0

    mini = float('inf')
    for k in range(i,j+1):
        steps = cuts[j+1]-cuts[i-1] + min_cost_cut_stick(i,k-1) + min_cost_cut_stick(k+1,j)
        mini = min(steps,mini)
    return mini

print(min_cost_cut_stick(1,c))    

#Memoization
def min_cost_cut_stick(i,j,dp):
    if i > j:
        return 0

    if dp[i][j] == -1:
        mini = float('inf')
        for k in range(i,j+1):
            steps = cuts[j+1]-cuts[i-1] + min_cost_cut_stick(i,k-1,dp) + min_cost_cut_stick(k+1,j, dp)
            mini = min(steps,mini)
        dp[i][j] = mini
    return dp[i][j]

dp = [[-1 for i in range(c+1)] for j in range(c+1)]
print(min_cost_cut_stick(1,c,dp))    

#Tabulation
dp = [[0 for i in range(c+2)] for j in range(c+2)]

for i in range(c,0,-1):
    for j in range(i,c+1):
        mini = float('inf')
        for k in range(i,j+1):
            steps = cuts[j+1]-cuts[i-1] + dp[i][k-1] + dp[k+1][j]
            mini = min(steps, mini)
        dp[i][j] = mini
print(dp[1][c])
