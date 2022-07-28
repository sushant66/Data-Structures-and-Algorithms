"""
Lowest Common Ancestor

	2
  3   4
5  6

LCA(3,4) = 2
LCA(3,6) = 3


Algo: if root == p or q or null then return root left call right call
		if left and right that means parent is lca hence return root
		else return left or root
"""


def lca(root,p,q):
	if not root or root == p or root == q:
		return root
	
	left = f(root.left,p,q)
	right = f(root.right,p,q)
	
	if left and right:
		return root
	
	return left or right

print(lca(root,p,q).val)
