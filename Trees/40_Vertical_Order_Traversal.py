"""
Vertical Order traversal 

eg see below tree
output - [[4],[2],[1,5,6],[3],[7]]


Algo: Keep a queue for traversal and keep a dict of list. Dict will store the nodes at that level along with vertical level. keep start and end for width. Do BFS keep node, horizontal level, vertical level. If two nodes are at same vertical level then sort according to their value.

"""

"""
     1
   2   3
  4 5 6 7
"""

def verticalTraversal(root):
    q = deque()
    q.append((root,0,0))
    d = defaultdict(list)
    start = float('inf')
    end = -float('inf')
    while q:
        size = len(q)
        for i in range(size):
            x,hl,vl = q.popleft()
            d[hl].append((vl,x.val))
            start = min(hl,start)
            end = max(hl,end)
            if x.left:
                q.append((x.left,hl-1,vl+1))
            if x.right:
                q.append((x.right,hl+1,vl+1))
    
    
    ans = []
    for i in range(start,end+1):
        ans+=[[j for i,j in sorted(d[i])]]
    return ans
