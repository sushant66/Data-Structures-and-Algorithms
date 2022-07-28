"""
Bottom view of binary Tree

for below eg
output = 4 2 5 6 3 7


Algo:   Use level order traversal
		use queue with pair (node, line)
		for below eg there will 4 lines -2 -1 0 1 2
		use dictionary for store line->val
		if not in dictionary then only insert (for top view) exclude for bottom view
		iterate from min to max to get top view

"""



#Tree definition
class TreeNode():
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

"""
     1
   2   3
  4 5 6 7
"""



from collections import deque

queue = deque()

queue.append((root,0))
d = {}

start = float('inf')
end = -float('inf')
while queue:
    size = len(queue)
    
    for i in range(size):
        data = queue.popleft()
        node = data[0]
        line = data[1]
        start = min(line, start)
        end = max(line, start)
       
        d[line] = node.val
        
        if node.left:
            queue.append((node.left,line-1))
        if node.right:
            queue.append((node.right,line+1))

for i in range(start,end+1):
    print(d[i])
