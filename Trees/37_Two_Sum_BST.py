"""
Two sum in BST

Given target find two nodes which sum up to the target.

ALgo: 1. take inorder are calculate two sum using 2 pointers.  (TC O(n)  SC O(N))
2. use next and before. next in BST iterator. store all left then go right then again all left exact opposite for before. store all right then left then all right. 
So just like two pointer i = next j = before then same as two sum.

"""
class BSTIterator:

    def __init__(self, root, reverse):
        self.stack = []
        self.reverse = reverse
        self.push_all(root)

    def next(self) -> int:
        node = self.stack.pop()
        if self.reverse: 
	        self.push_all(node.left)
        else:
        	self.push_all(node.right)
        return node.val
    
    def push_all(self,node):
        while node:
            self.stack.append(node)
            if self.reverse:
                node = node.right
            else:
                node = node.left
    
    def hasNext(self) -> bool:
        return len(self.stack) != 0
        
        
def find_target(root,k):
	if not root: return False
	l = BSTIterator(root,False)
	r = BSTIterator(root,True)
	
	i = l.next()
	j = r.next()
	while i < j:
		if i+j == k: return True
		elif (i+j) < k:
			i = l.next()
		else:
			j = r.next()
			
	return False
	
	


	


