__author__ = "Cody Swain"

class Solution(object):
	def get_two_sum(self, array, two_sum):
		previous_nums = dict()
		for index, num in enumerate(array):
			complement = two_sum - num
			if complement in previous_nums:
				return previous_nums[complement], index
			else: 
				previous_nums[num] = index

		return -1

if __name__ == "__main__":
	test_array = [1, 4, 5, 3, 6, 8, 9, 2, 10, 13]
	print("Indices of two numbers which give sum: {}".format(Solution().get_two_sum(test_array, 14)))