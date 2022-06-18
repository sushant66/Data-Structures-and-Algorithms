"""
Ninja Training
    Given n*3 matrix find max training points you can get provided no training on same index 
    in continous days

    eg:
        [10,50,1]      if you start with 10 you cant pick 5 in next day
        [5,100,2]


    ans = 10+100 = 110


           f(3,3)
    f(2,0)  f(2,1)  f(2,2)

f(1,1), f(1,2)

"""



tasks = [
    [10,50,1],
    [5,100,2]
]

#Recursion
def ninja_training(tasks, day, last):
    if day == 0:
        maxi = 0
        for i in range(0,3):
            if i != last:
                maxi = max(maxi, tasks[0][i])           #as day is 0
        return maxi
    
    maxi = 0
    for i in range(0,3):
        if i != last:
            points = tasks[day][i] + ninja_training(tasks, day-1, i)   #current + previous days points
            maxi = max(maxi, points)
    return maxi

print(ninja_training(tasks, len(tasks)-1, 3))    #last = 3 bcoz we can search in all 3


#Memoization
dp = [[-1 for j in range(3+1)] for i in range(len(tasks)+1)]
def ninja_training(tasks, day, last, dp):
    if day == 0:
        maxi = 0
        for i in range(0,3):
            if i != last:
                maxi = max(maxi, tasks[0][i])           #as day is 0
        return maxi
    
    if dp[day][last] != -1:
        return dp[day][last]

    maxi = 0
    for i in range(0,3):
        if i != last:
            points = tasks[day][i] + ninja_training(tasks, day-1, i, dp)   #current + previous days points
            maxi = max(maxi, points)
    dp[day][last] = maxi
    return dp[day][last]

print(ninja_training(tasks, len(tasks)-1, 3, dp))    #last = 3 bcoz we can search in all 3

#Tabulation
dp = [[0 for j in range(3+1)] for i in range(len(tasks))]
for i in range(4):          #col+1
    maxi = 0
    for j in range(3):      #col
        if i != j:
            maxi = max(maxi, tasks[0][j])
    dp[0][i] = maxi

for day in range(1,2):      #days
    for last in range(4):   #col+1
        maxi = 0
        for i in range(2):  #days
            if i != last:
                points = tasks[day][i] + dp[day-1][i]
                maxi = max(points, maxi)
    dp[day][last] = maxi

print(dp)
print(dp[1][3])             #n-1, column+1


#Space optimization
# as we just need previous we will keep only 1d array
dp = [0 for j in range(3+1)]
for i in range(4):          #col+1
    maxi = 0
    for j in range(3):      #col
        if i != j:
            maxi = max(maxi, tasks[0][j])
    dp[i] = maxi

for day in range(1,2):      #days
    temp = [0 for i in range(4)]
    for last in range(4):   #col+1
        for i in range(2):  #days
            if i != last:
                temp[last] = max(tasks[day][i] + dp[i], maxi)
    dp = temp

print(dp)
print(dp[3])             #n-1, column+1
