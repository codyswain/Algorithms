__author__ = "Cody Swain"

import sys

class Algorithm():
	def print_unordered_pairs(self, arr):
		'''This algorithm prints out half of an NxN array. Since you
		ignore coefficients in (N^2)/2, this algorithm has a time
		complexity of O(N^2).

		Parameters
		----------
		arr : array of numerical values
		'''
		for i in range(len(arr)):
			for j in range(i+1, len(arr)):
				sys.stdout.write("({}, {}) ".format(arr[i], arr[j]))
			sys.stdout.write("\n")

if __name__ == "__main__":
	array = [1,2,3,4,5,6,7,8,9,10]
	Alg = Algorithm()
	Alg.print_unordered_pairs(array)