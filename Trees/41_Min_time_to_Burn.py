"""
Minimum Time taken to burn the binary tree from a node


Approach: 1. Mark the parent pointer using hasmap with BFS. 
		  2. Add the start in q and do bfs and keep a flag set it 1 if node burnt
		  3. if flag then increment count
"""

def amountOfTime(root, start):    
    q = deque([root])
    d = {}
    starting = None
    while q:
        k = len(q)
        for i in range(k):
            node = q.popleft()
            if node.val == start:
                starting = node
            if node.left:
                d[node.left] = node
                q.append(node.left)
                
            if node.right:
                d[node.right] = node
                q.append(node.right)
                
    q = deque([starting])
    vis = set()
    ans = 0
    while q:
        flag = 0
        for i in range(len(q)):
            node = q.popleft()
            
            if node.left and node.left not in vis:
                q.append(node.left)
                flag = 1

            if node.right and node.right not in vis:
                q.append(node.right)
                flag = 1

            if node in d and d[node] not in vis:
                q.append(d[node])
                flag = 1

            vis.add(node)
        if flag:
            ans +=1
        
    return ans
         
    
    
    
    
    
    
