"""
Diameter of Binary Tree

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root

Algo:  Use logic of height of tree take a count variable 
		count = max(count, l+r) 

"""

count = 0

def diamter_of_tree(root):
	if not root:
		return 0
		
	l = diamter_of_tree(root.left)
	r = diamter_of_tree(root.right)
	global count
	count = max(count, l+r)
	return 1 + max(l,r)
	
print(diamter_of_tree(root))
	



