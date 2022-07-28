"""
Balanced Binary Tree

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Algo:  Same as height of binary tree except in the function if abs(l-r)>1 return -1 and in function call itself check if l == -1 or r == -1 return -1

"""


def balanced_binary_tree(root):
	if not root:
		return 0
		
	l = balanced_binary_tree(root.left)
	if l == -1: return -1    #Efficient approach as it saves time by not calling right
	r = balanced_binary_tree(root.right)
	if r == -1: return -1     
	
#	if l == -1 or r == -1:        
#		return -1
	
	if abs(l-r) > 1: return -1
	return 1 + max(l,r)   # Same as height of tree
	
print(True if balanced_binary_tree(root)!= -1 else False)
