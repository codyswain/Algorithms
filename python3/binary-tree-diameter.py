'''
Cody Swain
Leetcode Problem: #543, Diameter of Binary Tree
Difficulty: Easy
'''

# Definition for a binary tree
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def __init__(self):
		self.visited = []
		
	def diameter_of_binary_tree(self, root: TreeNode) -> int:
		self.diameter = 0
		self.get_depth(root)
		return self.diameter

	def get_depth(self, node):
		if not node: return 0
		l, r = self.get_depth(node.left), self.get_depth(node.right)
		self.diameter = max(self.diameter, l+r)
		return 1 + max(l, r)

	def in_order_traversal(self, root):
		if root.left: self.in_order_traversal(root.left)
		self.visited.append(root.val)
		if root.right: self.in_order_traversal(root.right)

	def get_traversal_results(self):
		return self.visited

if __name__ == "__main__":
	root = TreeNode(0)
	n1 = TreeNode(1)
	n2 = TreeNode(2)
	n3 = TreeNode(3)
	n4 = TreeNode(4)
	n5 = TreeNode(5)
	root.left = n3
	root.right = n5
	n3.left = n2
	n3.right = n4
	n2.left = n1

	sol = Solution()

	# Traverse tree in order
	sol.in_order_traversal(root)
	print("In order traversal results: {}".format(sol.get_traversal_results()))

	# Get longest path between two nodes in tree
	diameter = sol.diameter_of_binary_tree(root)
	print("Diameter: {}".format(diameter))
	
	
