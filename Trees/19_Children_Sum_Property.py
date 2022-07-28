"""
Children Sum Property

the sum of children must be equal to parent
you can increase the value of children by 1 unlimited times to make value of parent



"""


def children_sum(root):
	if not root:
		return
		
	child = 0
	
	if root.left:
		child += root.left.val
	if root.right:
		child += root.right.val
	
	if child > root.val:
		root.val = child
	else:
		if root.left:
			root.left.val = root.val
		
		if root.right:
			root.right.val = root.val
			
		
	children_sum(root.left)
	children_sum(root.right)
	
	total = 0
	if root.left:
		total += root.left.val
	if root.right:
		total += root.right.val
	if root.left or root.right:		#check for leaf node
		root.val = total

	
			
