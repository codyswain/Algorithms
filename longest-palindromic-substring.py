'''Cody Swain 
Leetcode Problem: #5 Longest Palindromic Substring'''

import numpy as np

class Solution():
	def dynamic_programming_solution(self, s: str) -> str:
		''' This solution is not complete'''
		length = len(s)
		palindrome = np.zeros((length, length+1), dtype=bool)

		# Fill in dp matrix for lengths 1 and 2
		for i in range(length):
			palindrome[i][1] = True
			if i < length-1:
				if s[i] == s[i+1]:
					palindrome[i][2] = True

		# Incrementally go over 3 letter palindromes, 4 letter palindromes, ....
		for k in range(3, length):

			# Go through each letter in the string
			for i in range(length):
				# Skip when position + length of substring palindrome
				# is greater than overall length
				if k + i > length-1:
					print("GREATER i:{}, k:{}".format(i, k))
					continue
				print("<=>i: {}\nk: {}\nchar: {}".format(i, k, s[i]))

				if s[i] == s[i+k-1] and palindrome[i+1][k-2]:
					print("Palindrome from: {}".format(s[i:i+k]))
		print(palindrome)

	def expand_from_center_solution(self, s: str) -> str:
		''' 
		This solution works.

		Time complexity: O(N^2). For each element in the for loop you
		have a worst case expansion of the whole strin O(N*N)

		Space Complexity: Ideally it should be O(1). You don't save an NxN 
		matrix like in the dynamic programming solution. In this case however,
		it is probably  worst case O(N^2) because I have to allocated space
		for a new string copy every time. 

		Improvements: 
		------------------------------------------------------------------------
		The while loops could be placed
		into a separate helper function to remove code redundancy.

		You also could save the indices instead of constantly creating
		copies of the string via temp (strings are immutable in python)
		which means a copy of the object is created. 
		''' 
		length = len(s) 
		longest = ""
		temp = ""
		for i in range(length):
			l = i
			r = i

			# Expand from individual chars
			while l>=0 and r<=length-1 and s[l]==s[r]:
				if s[l] == s[r]:
					temp = s[l:r+1]
					print("Temp 1st: {}".format(temp))
				if len(temp) > len(longest):
					longest = temp
				l -= 1
				r += 1

			# Expand from in between 2 char palindrome
			if i+1 <= length-1:
				if s[i] == s[i+1]:
					l = i
					r = i+1
					while l>=0 and r<=length-1 and s[l]==s[r]:
						temp = s[l:r+1]
						if len(temp) > len(longest):
							longest = temp
						l -= 1
						r += 1
					
		return longest
					
		
if __name__ == "__main__":
	test_str = "babaadaa"
	sol = Solution()
	longest_palindrome = sol.expand_from_center_solution(test_str)
	print(longest_palindrome)
		
