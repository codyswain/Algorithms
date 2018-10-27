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

if __name__ == "__main__":
	print(Solution().check_unique_chars("qwertyuiop"))
