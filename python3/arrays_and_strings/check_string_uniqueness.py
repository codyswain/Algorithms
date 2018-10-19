__author__ = "Cody Swain"
# Solution makes use of the fact that list lookup in python
# (if a in b) has a runtime complexity of O(n) while
# set lookup has a runtime complexity of O(1)

class Solution(object):
	def is_unique_string(self, str):
		if len(str) > 128: 	# 128 chars in normal ascii
			return False	# 256 chars in extended ascii
							# Unicode would be 1,114,112
		existing_chars = set()
		for char in str:
			if char in existing_chars:
				return False
			else:
				existing_chars.add(char)
		return True


if __name__ == "__main__":
	print(Solution().is_unique_string("helo"))
	print(Solution().is_unique_string("hello"))