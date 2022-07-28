"""

Insert in Binary Search Tree


Algo: We will insert the node after the leaf node only. so go to leaf as per the val
	if val < key insert to left else insert to right


TC - O(h) - O(logn)
"""


def insert(root,val):
	if not root:
		root = TreeNode(val)
		return root
		
	cur = root
	while cur:
		if val < cur.val:
			if cur.left:
				cur = cur.left
			else:
				cur.left = TreeNode(val)
				break
		else:
			if cur.right:
				cur = cur.right
			else:
				cur.right = TreeNode(val)
				break
	return root
	

def f(root,val):
    if not root:
        return TreeNode(val)
        
    if val < root.val:
        root.left = f(root.left,val)
    else:
        root.right = f(root.right,val)
    
