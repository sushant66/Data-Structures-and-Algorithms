"""
Maximum Path sum of binary tree

The path sum of a path is the sum of the node's values in the path.

Path may or may not pass through root


Algo: Use logic from height of binary tree 
	  calculate path max as max(val, val+left, val+right)
	  calculate max sum as max(maxsum, l+r+val,pathmax)
	  
"""

maxsum = root.val
def max_path_sum(root):
	if not root:
		return 0
		
	
	l = max_path_sum(root.left)
	r = max_path_sum(root.right)
	pathmax = max(root.val, root.val+root.left, root.val+root.right)
	maxsum = max(l+r+root.val, maxsum, pathmax)
	
	return pathmax

print(max_path_sum(root))
