"""
Serialize and Deserialize Binary Tree


Algo: Use level order traversall to store the data in string.
		For deserialize create root from first index take index = 1 put root in queue 
		pop from q check if its # then assign left add to q again else set none increment i do for right
"""


def serialize(root):
	
	q = deque([root])
	ls = []
	while q:
		node = q.popleft()
		
		if not node:
			ls.append('#')
		else:
			ls.append(str(node.val))
		
		if node:
			q.append(node.left)
			q.append(node.right)

	
	return ",".join(ls)
	

def deserialize(data):
	ls = data.split(',')	
	root = TreeNode(ls[0])
	
	q = deque([root])
	i = 1
	while q:
		node = q.popleft()
		
		if ls[i] == '#':
			node.left = None
		else:
			node.left = TreeNode(int(ls[i]))
			q.append(node.left)
		i+=1
		
		if ls[i] == '#':
			node.right = None
		else:
			node.right = TreeNode(int(ls[i]))
			q.append(node.right)
		i+=1
		
	return root
		
		
		
