"""
Construct BST from preorder traversal


eg 8 5 1 7 10 12
3 ways to do
1. Brute force take 8 now 5 will be at left then take 1 compare with 8 then with 5 ...
O(N*N)
2. Sort the list to get inorder. Then use preorder inorder to contruct tree just like Binary Tree  O(NLogN)
3. Use logic of validate BST O(N)

"""

i = 0
def construct(bound):
	nonlocal i
	if i == len(preorder) or preorder[i] > bound:
		return 
	
	root = TreeNode(preorder[i])
	i+=1
	root.left = construct(root.val)
	root.right = construct(bound)
	return root

preorder = [8,5,1,7,10,12]
construct(float('inf'))

	
