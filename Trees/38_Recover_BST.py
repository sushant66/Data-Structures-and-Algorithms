"""
Recover BST 
Given a tree recover bst by putting node at correct position where exactly 2 nodes of tree are swapped by mistake


Algo: 1. do inoreder. sort the list and then traverse through tree and if the elem at inorder is not equal to node change it with inorder value.  TC O(2n + nlogn) SC O(n)

2. keep prev, first, middle, last
prev - previous node first - first violoation middle second and last third
2 swap case 1. when nodes are not adjacent 2. when nodes are adjacent

for 1. first = prev middle = root and last swap first and last.
2. swap first and middle

"""


def inorder(root):
	nonlocal prev, first,middle,prev
	if not root:
		return
		
	inorder(root.left)
	if prev and root.val < prev.val:
		if not first:
			first = prev
			middle = root
		else:
			last = root
		
	
	prev = root
	inorder(root.right)

def recover(root):
	
	prev = TreeNode(-float('inf'))
	first = None
	middle = None
	last = None
	inorder(root)
	if first and last:
		first.val, last.val = last.val, first.val
	elif first and middle:
		first.val, middle.val = middle.val, first.val
	
	
		
	

