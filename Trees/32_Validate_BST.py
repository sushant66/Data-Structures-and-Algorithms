"""


Validate BST

Algo: We need to provide range of left and right so initially left = -float('inf) and right = float('inf')
"""


def validate_bst(root):
	
	def f(root,left,right):
		if not root: 
			return True
		
		if root.val >= right or root.val <= left:
			return False	
	
	
		return f(root.left,left,root.val) and f(root.right,root.val,right)
	
	return f(root,-float('inf'),float('inf'))
	
