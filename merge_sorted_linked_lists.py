# Cody Swain 
# ------------------------------
# Merge two singly linked lists
# ------------------------------

class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		self.next_node = new_next


class LinkedList(object):
	def __init__(self, head=None):
		self.head = head

	def insert(self, data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node

	def display(self):
		current = self.head
		while current is not None:
			print(current.get_data())
			current = current.get_next()

class Solution:
	def mergeTwoLists(self, l1: LinkedList, l2: LinkedList) -> LinkedList: 
		merged_list = LinkedList()
		l1_curr_node = l1.head
		l2_curr_node = l2.head

		while (l1_curr_node != None or l2_curr_node != None):

			# Case 1: if one list is empty, append all content of the other
			if l1_curr_node == None:
				while l2_curr_node != None:
					merged_list.insert(l2_curr_node.get_data())
					l2_curr_node = l2_curr_node.get_next()
				return merged_list
			elif l2_curr_node == None:
				while l1_curr_node != None:
					merged_list.insert(l1_curr_node.get_data())
					l1_curr_node = l1_curr_node.get_next()
				return merged_list

			l1_curr_val = l1_curr_node.get_data()
			l2_curr_val = l2_curr_node.get_data()

			# Case 2
			if l1_curr_val < l2_curr_val:
				merged_list.insert(l1_curr_val)
				l1_curr_node = l1_curr_node.get_next()

			# Case 3
			if l1_curr_val >= l2_curr_val:
				merged_list.insert(l2_curr_val)
				l2_curr_node = l2_curr_node.get_next()

		return merged_list

	def merge_two_lists(self, l1: LinkedList, l2: LinkedList) -> LinkedList:
		'''Revisited. This solution was procured in 8 minutes'''
		node = ListNode(None)
		merged = node

		while l1 or l2:
			if not l1:
				new_node = ListNode(l2.val)
				node.next = new_node
				l2 = l2.next
				node = node.next
			elif not l2:
				new_node = ListNode(l1.val)
				node.next = new_node
				l1 = l1.next
				node = node.next
			else:
				if l1.val < l2.val:
					new_node = ListNode(l1.val)
					node.next = new_node
					l1 = l1.next
					node = node.next
				else:
					new_node = ListNode(l2.val)
					node.next = new_node
					l2 = l2.next
					node = node.next


if __name__ == "__main__":

	# Singly linked list is FILO (First-In-Last-Out)
	list1 = LinkedList()
	list1.insert(87)
	list1.insert(69)
	list1.insert(16)
	list1.insert(13)
	list1.insert(7)
	list1.insert(1)
	# list1.display()

	list2 = LinkedList()
	list2.insert(100)
	list2.insert(99)
	list2.insert(68)
	list2.insert(43)
	list2.insert(12)
	list2.insert(6)
	# list2.display()

	merged_list = Solution().mergeTwoLists(list1, list2)
	merged_list.display()


