"""
Inorder successor in BST

Return the next element in inorder given a key node

Algo:  2 Approaches
1. Store inorder traversal then return next elem of given key node  O(N)
2. O(H) search the node and if any value greater the node val store in succesor
"""


def inorder_succesor(root, p):
	successor = None
	
	while root:
		if p.val >= root.val:
			root = root.right
		else:
			successor = root
			root = root.left
		
	return successor
		
	

	
