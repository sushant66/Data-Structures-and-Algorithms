"""
Symmetrical Tree

Check if left half of tree is an exact mirror of right half of tree


Algo:  root is always symmetric start from root.left and root.right
		check if both are none at same time else false
		if val doesnt match then false
		return left.left, right.right and inverse
"""





def symmetry_tree(left,right):
	if not left and not right:
		return True
		
	if not left or not right:
		return False
		
	if left.val!=right.val:
		return False
	
	return symmetry_tree(left.left,right.right) and symmetry_tree(left.right,right.left)
	

print(symmetry_tree(root.left,root.right))
