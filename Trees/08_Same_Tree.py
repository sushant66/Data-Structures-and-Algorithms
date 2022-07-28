"""
Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


Algo: go on left right of both if  not p and not q return True if not p or not q return False if p.val != q.val return False return call left of both and call left of right


"""

def same_tree(left,right):
	if not left and not right:
		return True

	if not left or not right:
		return False
	
	if left.val != right.val:
		return False
		
	return same_tree(left.left, right.left) and same_tree(left.right, right.right)

print(same_tree(p,q))


def same_tree(left,right):

	if not left or not right:
		return left == right
		
	return left.val == right.val and same_tree(left.left, right.left) and same_tree(left.right, right.right)

print(same_tree(p,q))
		
		
