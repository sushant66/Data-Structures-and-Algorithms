"""
Longest String Chain
words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]

Output = 5
All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"]



Algo:  Sort the word list as per length as we need sequence not subsequence
		Same as lis just replace arr[i]> arr[j] with check function 
		Check function checks if len of s1 == len of s2+1 and two pointers reach the end
		eg bc bca increment when equal and increment first when not equal
		both will point len

"""



words.sort(key=len)

def check(s1,s2):
    if len(s1) != len(s2)+1: return False
    
    first = 0
    second = 0
    
    while first < len(s1):
        if second < len(s2) and s1[first] == s2[second]:
            first+=1
            second+=1
        else:
            first+=1
    
    if first == len(s1) and second == len(s2): return True
    return False



dp = [1 for i in range(len(words))]
maxi = 1
for i in range(1,len(words)):
    for j in range(i):
        if check(words[i], words[j]) and 1+dp[j] > dp[i]:
            dp[i] = max(1+dp[j], dp[i])
        
    maxi = max(dp[i],maxi)

return maxi


#TC: O(N*N*L)


#Method 2
words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
words.sort(key=len)  # sort words by its length
ans = 0
from collections import defaultdict
dp = defaultdict(int)
for word in words:
    dp[word] = 1
    for i in range(len(word)):
        predecessor = word[:i] + word[i+1:]
        if predecessor in dp and dp[word] < dp[predecessor] + 1:
            dp[word] = dp[predecessor] + 1
    ans = max(ans, dp[word])
print(ans)
#TC: O(N*L*L)


