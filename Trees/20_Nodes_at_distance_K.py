"""

Print all nodes at distance k from given node


Algo: First mark the parents of all nodes in dict using BFS.
	  Add the target node to queue and spread outwards i.e left right up
	  add visited nodes to set. And at each step increment dist
	  if dist == k break store val of all nodes in q to res 
	
"""



def nodes_at_distance_k(root):
	q = deque([root])
    d = {root:None}
    while q:
        s = len(q)
        for i in range(s):
            node = q.popleft()
            
            if node.left:
                d[node.left] = node 
                q.append(node.left)
            if node.right:
                d[node.right] = node
                q.append(node.right)
    
    q = deque([target])
    dist = 0
    vis = set([target])
    while q:
        s = len(q)
        if dist == k:
            break
        dist+=1
        for i in range(s):
            node = q.popleft()
            left = node.left
            right = node.right
            up = d[node]
            
            if left and left not in vis:
                q.append(left)
                vis.add(left)
            if right and right not in vis:
                q.append(right)
                vis.add(right)
            if up and up not in vis:
                q.append(up)
                vis.add(up)
   
    res = []
    for i in q:
        res.append(i.val)
    return res
