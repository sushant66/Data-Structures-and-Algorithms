"""
Buy sell stock with a transaction fee

prices = [1,3,2,8,4,9], fee = 2
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Algo: Same as buy sell stock 2 just do prices[i]-fee in not buy

"""




n = len(prices)
prev_buy = 0
prev_not_buy = 0
for i in range(n-1,-1,-1):  
    curr_buy = max(-prices[i]+prev_not_buy, prev_buy)
    curr_not_buy = max(prices[i]-fee+prev_buy, prev_not_buy)
    
    prev_buy = curr_buy
    prev_not_buy = curr_not_buy

return prev_buy
