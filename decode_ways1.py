# Cody Swain
# Date: 8/2/19
# Leetcode problem: Decode Ways
# Difficulty: Medium

''' Problem Statement:
The following encoding exists: 1->'A', 2->'B, 3->'C', ... 26->'Z'
Given a string of numbers, return the number of ways the string may be decoded
'''

class Solution:
	def decode_ways(self, number_string):
		count = [0] * (len(number_string)+1)
		count[0] = 1
		count[1] = 1 if number_string[0] != "0" else 0

		for idx in range(2, len(number_string)+1):
			if int(number_string[idx-1]) != '0':
				count[idx] = count[idx-1]

			if int(number_string[idx-2])<=2 and int(number_string[idx-1])<=6:
				count[idx] += count[idx-2]

		return count[len(number_string)]
		
if __name__ == "__main__":
	number_str = "12129"
	sol = Solution()
	print(sol.decode_ways(number_str))
