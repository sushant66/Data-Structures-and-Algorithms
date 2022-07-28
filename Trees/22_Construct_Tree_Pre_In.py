"""
Construct a Tree from preorder and inorder Traversal

ALgo: First index of preorder will always be the tree root
	 Find the elem in inorder list and divide it 
	 Store the elem of inorder and its index in hashmap


"""

#Preorder - Root left right   -- right = left+1 
#inorder - left root right 

def construct(inorder,preorder):
	
	d = {}
	for i in range(len(inorder)):
		d[inorder[i]] = i
	
	def f(prestart,preend,instart,inend):
		if prestart > preend or instart > inend:
			return 
		
		root = TreeNode(preorder[prestart])
		inroot = d[root.val]
		numsleft = inroot-prestart
		
		root.left = f(prestart+1,prestart+numsleft,instart,inroot-1)
		root.right = f(prestart+numsleft+1,preend, inroot+1,inend)
		return root
		
	return f(0,len(preorder)-1,0,len(inorder)-1)


