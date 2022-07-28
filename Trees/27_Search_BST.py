"""
Search in BST 


"""



def search(root,val):
	while root and root.val!=val:
		if val < root.val: root = root.left
		else: root = root.right
	return root
