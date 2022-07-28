"""
Delete Node from BST

Algo: 2 ways. search the node detach the left part and assign it to right's leftmost nodes left  
	or detach right part and assign it to left's rightmost nodes right	

Below is 1st approach
"""


def delete_node(root,val):
	if not root:
		return None
	
	if root.val == key:
		return helper(root)
		
	dummy = root
	
	while root:
		if root.val > key:
			if root.left and root.left.val == key:
				root.left = helper(root.left)
				break
			else:
				root = root.left
		else:
			if root.right and root.right.val == key:
				root.right = helper(root.right)
				break
			else:
				root = root.right

		return dummy
		
def helper(root):
	if not root.left:
		return root.right
	elif not root.right:
		return root.left
	
	right = root.right
	cur = root.left
	while cur.right:
		cur = cur.right
	cur.right = right
	return root.left


#detach left and assign to right

# Recursive

def f(root,key):
	if not root:
		return
	
	if root.val == key:
		if not root.left:
			return root.right
		if not root.right:
			return root.left
		if root.left and root.right:
			temp = root.right
			while temp.left:
				temp = temp.left
			root.val = temp.val
			root.right = f(root.right,root.val)
	elif root.val > key:
		root.left = f(root.left,key)
	else:
		root.right = f(root.right,key)
	return root

	
