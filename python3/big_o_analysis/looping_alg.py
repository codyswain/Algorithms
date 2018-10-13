__author__ = "Cody Swain"

import sys

class Algorithm():
	def print_unordered_pairs(self, arr):
		for i in range(len(arr)):
			for j in range(i+1, len(arr)):
				sys.stdout.write("({}, {}) ".format(arr[i], arr[j]))
			sys.stdout.write("\n")

if __name__ == "__main__":
	array = [1,2,3,4,5,6,7,8,9,10]
	Alg = Algorithm()
	Alg.print_unordered_pairs(array)