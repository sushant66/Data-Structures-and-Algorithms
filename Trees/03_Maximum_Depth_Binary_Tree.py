"""
Maximum Depth of binary tree (height of binary tree)


Algo:  Traverse the tree using dfs and if hit null return 0 else return 1 + max(left,right)

"""


def maximum_depth(root):
    if not root:
        return 0
    
    
    return 1 + max(maximum_depth(root.left), maximum_depth(root.right))

print(maximum_depth(root))
