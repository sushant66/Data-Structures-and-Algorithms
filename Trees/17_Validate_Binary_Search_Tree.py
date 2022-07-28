"""
Validate if given tree is BST

A valid BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.



ALgo: keep left=float('inf') and right = float('inf') we will fill this on the go and compare the nodes
	if left >= root.val or right <= root.val return False
	
	at last for left call take min(root.val,left), right and for right left, max(root.val,right)
	
"""


def validate_bst(root, left,right):
    if not root:
        return True
    
    if left <= root.val or right >= root.val:
        return False
    
    return validate_bst(root.left,min(root.val,left),right) and validate_bst(root.right,left,max(root.val,right))


return validate_bst(root,float('inf'), -float('inf'))
