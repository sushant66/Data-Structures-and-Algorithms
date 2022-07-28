"""
Kth smallest element in BST

Algo: Do inorder traversal and as soon as k == 0 store it in a variable

For Kth largest - find n-k th smallest or do right root left

"""


#Recursive
ls = []
def kth_smallest(root,k):
	
	if not root:
		return 
	
	f(root.left,k-1)
	if k == 0:
		ls.append(root.val)
	f(root.left,k-1)


#Iterative

def kth_smallest(root,k):
	
	stack = []
	curr = root
	while curr or stack:
		while curr:
			stack.append(curr)
			curr = curr.left
		
		curr = stack.pop()
		k-=1
		if k == 0:
			return curr.val
		curr = curr.right
	
