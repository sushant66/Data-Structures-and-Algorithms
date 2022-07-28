"""
Construct a Tree from postorder and inorder Traversal

ALgo: Last index of postorder will always be the tree root
	 Find the elem in inorder list and divide it 
	 Store the elem of inorder and its index in hashmap


"""

#Postorder - left right root        
#inorder - left root right 

def construct(inorder,postorder):
	
	d = {}
	for i in range(len(inorder)):
		d[inorder[i]] = i
	
	def f(poststart,postend,instart,inend):
		if poststart > postend or instart > inend:
			return 
		
		root = TreeNode(preorder[postend])
		inroot = d[root.val]
		numsleft = inroot-instart
		
		root.left = f(poststart,poststart+numsleft-1,instart,inroot-1)
		root.right = f(poststart+numsleft,postend-1, inroot+1,inend)
		return root
		
	return f(0,len(postorder)-1,0,len(inorder)-1)


