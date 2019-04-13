__author__ = "Cody Swain"

''' Strategy: 
    -------------------------------------------------------------------------------------------
	Loop over the values in the list. 
	For each element, calculate the necessary complement required to obtain the target
	Store the index of the element with the key as the complement
	When the complement is reached, return the value stored at key, and the idx of complement

	Complexity Analysis: 
	The runtime complexity is O(n) because in the worst case scenario, you do a linear scan
	of the entire list. Given a large ordered list, it may be beneficial to run a binary search 
	for the complement value. 
'''

class Solution(object):
	def twoSum(self, nums, target): 
		complements = {}
		for idx, val in enumerate(nums):
			if val in complements.keys():
				return complements[val], idx
			else:
				complements[target-val] = idx

if __name__ == "__main__":
	test_array = [1, 4, 5, 3, 6, 8, 9, 2, 10, 13]
	print("Indices of two numbers which give sum: {}".format(Solution().twoSum(test_array, 14)))