"""
Binary Tree Zigzag Level Order Traversal
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).


Algo: same as level order traversal keep a flag to decide from where to place values
	if flag then insert from end else from start
"""


def zigzag_traversal(root):
	if not root:
        return []
    
    queue = deque()
    queue.append(root)
    flag = False
    res = []
    while queue:
        size = len(queue)
        level = [0]*size 
        for i in range(size):
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
            k = i if not flag else size-i-1
            level[k] = node.val
        res.append(level)
        flag = not flag
    
    return res
    
print(zigzag_traversal(root))
