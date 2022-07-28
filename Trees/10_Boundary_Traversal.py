"""
Boundary traversal 

eg see below tree
output - 1 2 4 5 6 7 3


Algo: first get left boundary excluding leaf then get leaf using preorder traversal
	then get right boundary excluding leaf

	for left -- go to left until hit null then go to right and stop before leaf node
	same for right (store in stack and pop to get reverse)
	for leaves - do preorder traversal and when its leaf node then store val in res
"""




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


res = []

def is_leaf(root):
    if not root.left and not root.right:
        return True
    return False
    

def add_left(root):
    curr = root.left
    while curr:
        if not is_leaf(curr):
            res.append(curr.val)
        if curr.left:
            curr = curr.left
        else:
            curr = curr.right
    
def add_right(root):
    curr = root.right
    temp = []
    while curr:
        if not is_leaf(curr):
            temp.append(curr.val)
        if curr.right:
            curr = curr.right
        else:
            curr = curr.left
    
    for i in range(len(temp)-1,-1,-1):
        res.append(temp[i])
    

def add_leaves(root):
    if is_leaf(root):
        res.append(root.val)
        return
    
    add_leaves(root.left)
    add_leaves(root.right)


# Main 
if not root:
    print(res)
if not is_leaf(root):
    res.append(root.val)
add_left(root)
add_leaves(root)
add_right(root)
print(res)

    
    
        
            
