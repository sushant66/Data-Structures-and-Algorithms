"""

Morris Traversal 



Inorder, Preorder Traversal
Algo: 
	1. set curr = root
	2. check if curr has left if not then add the val to list and go to cur = cur.right
	3. else set prev = curr.left
	4. go to rightest node and it shouldnt point back to curr
	5. if prev has no right then create connection prev.right = curr and move curr to left
	6. if prev right is not null cut the connection prev.right = None add the val to list and go to curr = curr.right 

TC - O(N)
SC - O(1)
"""




def morris_traversal(root):
	curr = root
	inorder = []
	preorder = []
	while curr:
		if not curr.left:
			inorder.append(curr.val)
			preorder.append(curr.val)
			cur = cur.right
		else:
			prev = curr.left
			while prev.right and prev.right!=curr:
				prev = prev.right
			
			if not prev.right:
				prev.right = curr
				preorder.append(curr.val)
				curr = curr.left
			else:
				prev.right = None
				inorder.append(curr.val)
				curr = curr.right
				
	return inorder, preorder
			
				



