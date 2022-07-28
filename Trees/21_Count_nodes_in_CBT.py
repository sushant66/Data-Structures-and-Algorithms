"""
Count Total Nodes in Complete Binary Tree

In CBT all levels are filled except possibly the last



ALgo: So here nodes = 2^h - 1. Calculate height of left and right subtree if both equal the return 2**h -1.  At last 1 + f(root.left) + f(root.right)


Height will be log(n) 

Time Complexity = logn x logn   (Traversing * Calculating height)
Space = logn (Recursive stack space)
"""



def count_nodes(root):

	def left_height(node):
		h=0
		while node:
			h+=1
			node = node.left
		return h
		
	def right_height(node):
		h=0
		while node:
			h+=1
			node = node.right
		return h
		
	
	def f(root):
		if not root:
			return 0
			
		lh = left_height(root)
		rh = right_height(root)
		
		if lh == rh: return 2**lh-1
		
		return 1 + f(root.left) + f(root.right)
		
		
