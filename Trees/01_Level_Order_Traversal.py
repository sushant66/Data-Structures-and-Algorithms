
"""

ALgo: Use queue initally keep root in queue then loop till queue is empty
	  take len of queue as size and iterate over it pop the element from queue
	  check if right left present and add to queue add the node val to temp list
	  add temp list  to res list


"""




queue = collections.deque()
# queue = [root]
queue.append(root)
ls = []

while queue:
    size = len(queue)
    level = []
    for i in range(size):
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        
        level.append(node.val)
    ls.append(level)
return ls


#Using DFS

level = []
        
def dfs(root,h):
    if not root:
        return
    if h==len(level):
        level.append([])
    
    level[h].append(root.val)
    dfs(root.left,h+1)
    dfs(root.right,h+1)
dfs(root,0)
return level
