__author__ = "Cody Swain"

from merge_sort import MergeSort

'''Implement an algorithm to determine if a string has all unique characters
What if you cannot use additional characters?'''

class Solution(object):
	def check_unique_chars(self, input_str):
		if len(input_str) > 128:
			return False
		char_set = set()
		for char in input_str:
			if char in char_set:
				return False
			else:
				char_set.add(char)
		return True

	def check_unique_chars_without_stuctures(self, input_str):
		'''Check for unique chars without access to a set

		Method 1: Iterate through string and check for duplicate. This would
		be O(N^2) time.

		Method 2: Sort string and search through neighbor values. Sorting 
		could hypothetically be O(Nlog(N)) and then the comparison could be
		roughly O(N)'''

		# Not going to implement right now.
		return None


if __name__ == "__main__":
	print(Solution().check_unique_chars("qwertyuiop"))
