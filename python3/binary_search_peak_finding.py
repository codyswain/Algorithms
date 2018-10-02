__author__ = "Cody Swain"

import time
import math

## TO DO ##
# This algorithm is inefficient because it passes the whole array with each recursive pass.
# Memory usage can be reduced simply using the indices with a while loop. 

def binary_search(arr):
	'''Binary search peak finding for a one dimensional array
	Parameters
	----------
	arr : list
		List of numerical values with a peak.
	'''

	# Iteration metadata
	print("Length: {len} \t Array: {arr}".format(arr=arr, len=len(arr)))

	# Algorithm Implementation
	n = len(arr)
	if n%2 == 0:
		mid_idx = int(n/2-1)
	else: 
		mid_idx = int((n-1)/2)
	if arr[mid_idx] < arr[mid_idx-1]:
		return binary_search(arr[:mid_idx])
	elif arr[mid_idx] < arr[mid_idx+1]:
		return binary_search(arr[mid_idx:])
	else: 
		peak = arr[mid_idx]
		return peak

if __name__ == "__main__":
	# Test Array
	array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 18, 16, 14, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
	
	# Run binary search, and track runtime.
	print("\n\nBinary search peak finding algorithm. \n")
	start_time = time.time()
	peak = binary_search(array)
	end_time = time.time()
	print("\nPeak found: {}".format(peak))
	print("Execution time: {}s\n\n".format(end_time-start_time))