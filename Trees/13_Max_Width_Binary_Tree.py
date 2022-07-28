"""
The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.


Algo: level order traversal 
	  keep root at 0 in queue
	  for left add line*2 and for right add line*2 + 1
	  Take max of queue[-1][1] - queue[0][1] + 1   (max-min+1)

"""

from collections import deque

def max_width(root):
	queue = deque()
    
    queue.append((root,0))
    
    
    maxi = 0
    mini = 0
    res = 0
    while queue:
        size = len(queue)
        mini,maxi = queue[0][1], queue[-1][1]
        res = max(res, maxi-mini+1)
        for i in range(size):
            data = queue.popleft()
            node = data[0]
            line = data[1]

            if node.left:
                queue.append((node.left,line*2))
            
            if node.right:
                queue.append((node.right,line*2+1))
    return res
