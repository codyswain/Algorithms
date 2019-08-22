# Cody Swain 
# Date: 8/2/19
# Leetcode Problem: Add Two Numbers
# Difficulty: Medium

''' Problem Statement:
You are given two non-empty linked lists representing two non-negative integers
The digits are stored in reverse order and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list. 

You may assume the two numbers do not contain any leading zero, except the 
number 0 itself.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807'''

# Linked List Data Structure
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
		
class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		# Calculate sum and carry
		sum = l1.val + l2.val
		carry = 1 if sum >= 10 else 0
		sum = sum % 10

		# Add sum to result list
		root = ListNode(sum)
		prev = root #Create an alias to root node

		# Move to next node in linked list
		l1 = l1.next
		l2 = l2.next

		while l1 or l2 or carry == 1:
			if not l1 and not l2:
				sum = 1
			elif not l1:
				sum = carry + l2.val
				l2 = l2.next
			elif not l2:
				sum = carry + l1.val
				l1 = l1.next
			else:
				sum = l1.val + l2.val + carry
				l1 = l1.next
				l2 = l2.next

			# Calculate carry and sum
			carry = 1 if sum >= 10 else 0
			sum = sum % 10

			# Add sum to result and update prev node
			cur = ListNode(sum)
			prev.next = cur
			prev = prev.next

		return root

	
if __name__ == "__main__":
	# Initialize linked lists
	l1 = ListNode(2)
	l1_1 = ListNode(4)
	l1_2 = ListNode(3)
	l1.next = l1_1
	l1_1.next = l1_2

	l2 = ListNode(5)
	l2_1 = ListNode(6)
	l2_2 = ListNode(4)
	l2.next = l2_1
	l2_1.next = l2_2

	my_solution = Solution()
	res = my_solution.addTwoNumbers(l1, l2)
	print("Expected solution: 7 -> 0 -> 8")
	print("{num1} -> {num2} -> {num3}".format(num1=res.val, num2=res.next.val,
											  num3=res.next.next.val))
	
