"""
Min number of insertion/deletions required to convert string A to B

Eg - adshhk asdi      ans - 6


ALGO:
	(len(str1) - LCS(str1,str2)) + (len(str2) - LCS(str1,str2))
	(4 - 2) + (3-2) = 2 + 1 = 3

	adshhk asdi   4+2 = 6  LC - ad
"""

a1 = 'adshhk'
a2 = 'asdi'

def lcs(a1,a2):
	m = len(a1)
	n = len(a2)
	dp = [0 for i in range(n+1)]

	for i in range(m+1):
		temp = [0 for x in range(n+1)]
		for j in range(n+1):
		    if i==0 or j == 0:
		        temp[j] = 0
		    elif a1[i-1] == a2[j-1]:
		        temp[j] = 1 + dp[j-1]
		    else:
		        temp[j] = max(dp[j],temp[j-1])
		dp = temp

	return dp[n]

lcs_len = lcs(a1,a2)
print((len(a1)-lcs_len) + (len(a2)-lcs_len))

