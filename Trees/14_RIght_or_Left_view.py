"""
Binary Tree Right/Left Side View

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

ALgo: Can do using level order but length code hence use recursion 
	  Use preorder  (Root left right)  but in this case we will get LEFT view
	  for right view change order so (Root Right Left)
	  keep track of level and when len(res) == level add node

"""



def right_view(root, level):
	if not root:
		return
	
	if len(res) == level:
		res.append(root.val)
		
	right_view(root.right, level+1)	
	right_view(root.left, level+1)
	
	
res = []
print(right_view(root, 0))


def left_view(root, level):
	if not root:
		return
	
	if len(res) == level:
		res.append(root.val)
		
	left_view(root.left, level+1)
	left_view(root.right, level+1)		
	
res = []
print(left_view(root, 0))
