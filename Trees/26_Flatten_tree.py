"""
Flatten Tree to Linked list

List should be in pre order manner i.e root left right 
For tree.right = next node and tree.left = None

Algo:  Start from the depth of right subtree and then move to left and root
		right -> left -> root
		first do right left traversal then root.right = prev root.left = None
		prev = root


"""

self.prev = None
def flatten(root):
	if not root:
		return 
		
	flatten(root.right)
	flatten(root.left)
	
	root.right = self.prev
	root.left = None
	self.prev = root
	
flatten(root)




#Using stacks
def flatten(root):
	stack = []
	stack.append(root)
	
	while stack:
		curr = stack.pop()
		
		if curr.right:
			stack.append(curr.right)
		if curr.left:
			stack.append(curr.left)
			
		if stack:
			curr.right = stack.pop()
		curr.left = None
		
		
#3rd Method O(1) space

curr = root
while curr:
	if curr.left:
		prev = curr.left
		while prev.right:
			prev = prev.right
			
		prev.right = curr.right
		curr.right = curr.left
		
	curr = curr.right


			
			
		

