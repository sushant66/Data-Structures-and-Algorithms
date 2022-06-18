
"""
Evaluate Boolean Expression To True

Eg: T|T&F
ans = (T|T)&F = F  (T)|(T&F) = T so only 1 way 


Algo: start from 0 to j f(0,j) partition will be always on i+2 and we want true so isTrue = 1
        i+1 to j-1 with increment of 2
        if only single left then if it is what we want then return
        evaulate lt rt lf rf eg lt = f(i,k-1,1) rf = f(k+1,j,0)
        if k == & then if we want true ways+=lt * rt (1&1 = 1)else ways+= lt*rf+rt*lf+lf*rf
        multiply because of N to N mapping eg (lf 3 rf 3 then 1st lf with all 3 rf..)
        same for | and ^ return ways

"""

s = "T|T&F|T"           #(T|T)&(F|T)-1   (T)|(T&F|T) - 2  (T|T&F)|T - 2  

#Recursion
def evaulate(i,j,is_true):
    if i > j:
        return 0
    
    if i == j:
        if s[i] == 'T' and is_true:
            return 1
        if s[i] == 'F' and not is_true:
            return 1
        return 0

    ways = 0
    for k in range(i+1,j,2):
        lt = evaulate(i,k-1,1)
        lf = evaulate(i,k-1,0)
        rt = evaulate(k+1,j,1)
        rf = evaulate(k+1,j,0)

        if s[k] == '&':
            if is_true:
                ways += lt*rt
            else:
                ways += (lf*rf)+(lf*rt)+(lt*rf)
        elif s[k] == '|':
            if is_true:
                ways += (lt*rt)+(lf*rt)+(lt*rf)
            else:
                ways += (lf*rf)
        else:
            if is_true:
                ways += (lt*rf)+(rf*lt)
            else:
                ways += (lt*rt)+(lf*rf)
    return ways

print(evaulate(0,len(s)-1,1))

#Memoization
def evaulate(i,j,is_true,dp):
    if i > j:
        return 0
    
    if i == j:
        if s[i] == 'T' and is_true:
            return 1
        if s[i] == 'F' and not is_true:
            return 1
        return 0

    if dp[i][j][is_true] == -1:
        ways = 0
        for k in range(i+1,j,2):
            lt = evaulate(i,k-1,1,dp)
            lf = evaulate(i,k-1,0,dp)
            rt = evaulate(k+1,j,1,dp)
            rf = evaulate(k+1,j,0,dp)

            if s[k] == '&':
                if is_true:
                    ways += lt*rt
                else:
                    ways += (lf*rf)+(lf*rt)+(lt*rf)
            elif s[k] == '|':
                if is_true:
                    ways += (lt*rt)+(lf*rt)+(lt*rf)
                else:
                    ways += (lf*rf)
            else:
                if is_true:
                    ways += (lt*rf)+(rf*lt)
                else:
                    ways += (lt*rt)+(lf*rf)
        dp[i][j][is_true] = ways
    return dp[i][j][is_true]

n = len(s)
dp = [[[-1 for i in range(2)] for j in range(n)] for k in range(n)]
print(evaulate(0,n-1,1,dp))

#Tabulation
dp = [[[0 for i in range(2)] for j in range(n)] for k in range(n)]


for i in range(n):
    if s[i] == 'T':
        dp[i][i][1] = 1 
    if s[i] == 'F':
        dp[i][i][0] = 1

for i in range(n-1,-1,-1):
    for j in range(i,n):
        for x in range(i+1,j,2):
            lt = dp[i][x-1][1]
            rt = dp[x+1][j][1]
            lf = dp[i][x-1][0]
            rf = dp[x+1][j][0]
            if s[x] == '&':
                dp[i][j][1] += lt*rt
                dp[i][j][0] += (lf*rf)+(lf*rt)+(lt*rf)
            elif s[x] == '|':
               
                dp[i][j][1] += (lt*rt)+(lf*rt)+(lt*rf)
                dp[i][j][0] += (lf*rf)
            else:
                dp[i][j][1] += (lt*rf)+(rf*lt)
                dp[i][j][0] += (lt*rt)+(lf*rf)

print(dp[0][n-1][1])



#Tabulation
dp = [[[0 for i in range(2)] for j in range(n)] for k in range(n)]


for i in range(n):
    if s[i] == 'T':
        dp[i][i][1] = 1 
    if s[i] == 'F':
        dp[i][i][0] = 1

for i in range(n-1,-1,-1):
    for j in range(i,n):
        for is_true in range(2):
            ways = 0
            for x in range(i+1,j,2):
                lt = dp[i][x-1][1]
                rt = dp[x+1][j][1]
                lf = dp[i][x-1][0]
                rf = dp[x+1][j][0]
                if s[x] == '&':
                    if is_true:
                        ways += lt*rt
                    else:
                        ways += (lf*rf)+(lf*rt)+(lt*rf)
                elif s[x] == '|':
                    if is_true:
                        ways += (lt*rt)+(lf*rt)+(lt*rf)
                    else:
                        ways += (lf*rf)
                else:
                    if is_true:
                        ways += (lt*rf)+(rf*lt)
                    else:
                        ways += (lt*rt)+(lf*rf)
            dp[i][j][is_true] += ways                

print(dp[0][n-1][1])
