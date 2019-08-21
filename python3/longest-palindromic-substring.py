'''Cody Swain 
Leetcode Problem: #5 Longest Palindromic Substring'''

import numpy as np

class Solution():
	def longest_palindrome(self, s: str) -> str:
		length = len(s)
		if s == "" or length < 2:
			return s

		left = 0
		right = 0

		isPalindrome = [[False]*length]*length
		
		for j in range(length):
			for i in range(j):
				if j-1 <= 2:
					isInnerPalindrome = True
				elif isPalindrome[i+1][j-1]:
					isInnerPalindrome = True
				else:
					isInnerPalindrome = False

				if (s[i] == s[j] and isInnerPalindrome):
					isPalindrome[i][j] = True;

					if j-i > right-left:
						left = i
						right = j

		return s[left: right+1]

	def longest_palindromic_substring(self, s: str) -> str:
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
					
		
if __name__ == "__main__":
	test_str = "babaadaa"
	sol = Solution()
	sol.longest_palindromic_substring(test_str)
		
