"""
Print root to node path 

Given a node print the path from root to that node

Algo: if the root is null return false 
	append every root val to list and check if root val = x return true
	if left or right gives true return true
	backtracking remove last added element and return false

"""



def print_path(root,x):
	if not root:
		return False
		
	res.append(root.val)
	
	if root.val == x:
		return True
	
	if print_path(root.left,x) || print_path(root.right,x):
		return True
	
	res.pop()
	return False
	
res = []
print_path(root,x)
print(res)
