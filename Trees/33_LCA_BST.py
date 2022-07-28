"""

Lowest Common Ancestor of BST

Algo: if p and q both are small than root the search in left if both greater than root search in right else root is the lca 

TC - O(H)
"""


def lca_bst(root,p,q):
	def f(root,p,q):
		if not root:
			return root
			
		
		if p.val < root.val and q.val < root.val:
			return f(root.left,p,q)
		if p.val > root.val and q.val > root.val:
			return f(root.right,p,q)
		
		return root
	return f(root,p,q)
