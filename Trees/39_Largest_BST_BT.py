"""
Largest BST in a Binary Tree


Algo: 1. Use validate bst on every node and do any traversal to count length O(N^2)

2. Keep largest, smallest and start from bottom. Single node is always bst so start from there take smallest largest go up and compare if valid increase size. for it to be valid left largest < root.val < right smallest


"""

class Node:
	def __init__(min_node,max_node,size):
		self.min_node = min_node
		self.max_node = max_node
		sefl.size = size


def largest_bst_helper(root):
	if not root:
		return  Node(float('inf'),-float('inf'),0)
	
	left = largest_bst_helper(root.left)
	right = largest_bst_helper(root.right)
	#Current node is greater than left max and less than right min 
	if (left.max_node < root.val and root.val < right.min_node):
		return Node(min(root.val,left.min_node), max(root.val,right.max_node), 1+left.max_size+right.max_size)
	
	#pass such values that cannot be compared -> max -> inf min ->  (-inf)
	return Node(-float('inf'),float('inf'),max(left.max_size,right.max_size))
	

def largest_bst(root):
	return largest_bst_helper(root).max_size
		
	
