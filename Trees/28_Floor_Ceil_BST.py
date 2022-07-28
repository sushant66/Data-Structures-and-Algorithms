"""
Ceil Floor Binary search tree

Ceil - find the val which is greater than or equal to the key.

Floor - find the val which is smaller than or equal to the key.

Algo: for ceil store the ceil when key < val and for floor store floor when key > val
"""


def ceil_bst(root,key):
	ceil = -1
	
	while root:
		if root.val == key:
			ceil = root.val
			return ceil
		
		if key > root.val:
			root = root.right
		else:
			ceil = root.val
			root = root.left
	return ceil
	
def floor_bst(root,key):
	floor = -1
	
	while root:
		if root.val == key:
			floor = root.val
			return ceil
		
		if key > root.val:
			floor = root.val
			root = root.right
		else:
			root = root.left
	return floor
