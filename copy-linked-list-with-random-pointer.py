'''
Cody Swain
Leetcode problem: #138 Copy List with Random Pointer
Difficulty: Medium
'''

# Definition for a node
class Node:
	def __init__(self, val, next, random):
		self.val = val
		self.next = next
		self.random = random

class Solution:
	def __init__(self):
		self.visited = {}

	def copy_random_list(self, head: 'Node') -> 'Node':
		if not head:
			return None

		if head in self.visited.keys():
			return self.visited[head]

		new_node = Node(head.val, None, None)
		self.visited[head] = new_node

		new_node.next = self.copy_random_list(head.next)
		new_node.random = self.copy_random_list(head.random)
		return new_node
