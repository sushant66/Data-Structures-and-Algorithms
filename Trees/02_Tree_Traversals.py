
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

#Inorder Traversal
print("Inorder Traversal - ")
def inorder(root):
    if not root:
        return 
    
    inorder(root.left)
    print(root.val)
    inorder(root.right)

inorder(root)

#Preorder Traversal
print("Preorder Traversal - ")
def preorder(root):
    if not root:
        return 
    
    print(root.val)
    preorder(root.left)
    preorder(root.right)

preorder(root)


#Postorder Traversal
print("Postorder Traversal - ")
def postorder(root):
    if not root:
        return 
    
    postorder(root.left)
    postorder(root.right)
    print(root.val)

postorder(root)

# Keep adding node and go to left when hit none start popping and adding to ans and go to right
print("Inorder Stack")
def inorder_stack(root):
    node = root
    stack = []
    ls = []
    while True:
        if node:
            stack.append(node)
            node = node.left
        else:
            if not stack:
                break
            node = stack.pop()
            ls.append(node.val)
            node = node.right
    return ls

print(inorder_stack(root))


# Exact opposite root left right --> root right left
print("Preorder Stack")
def preorder_stack(root):
    stack = [root]
    ls = []
    while stack:
        node = stack.pop()
        ls.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return ls

print(preorder_stack(root))

#keep 2 stacks add root in stack1 and loop till its not empty pop element add to stack2 go to left right. At end pop stack2 and append to ans
print("Postorder Stack")
def postorder_stack(root):
    stack1 = []
    stack2 = []
    ls = []
    stack1.append(root)
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    
    while stack2:
        ls.append(stack2.pop().val)
    return ls

print(postorder_stack(root))


# Post order using 1 stack
#Go to left left left until hit none then go to right and again left left...

def post_order_1_stack(root):
    stack = []
    curr = root
    ls = []
    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            temp = stack[-1].right
            if not temp:
                temp = stack.pop()
                ls.append(temp.val)
                while stack and temp == stack[-1].right:
                    temp = stack.pop()
                    ls.append(temp.val)
            else:
                curr = temp
    return ls

print(post_order_1_stack(root))

