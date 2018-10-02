__author__ = "Cody Swain"

import time
import math
import numpy as np




def binary_search_2d(arr):
	'''Binary search peak finding for a two dimensional array
	Parameters
	----------
	arr : matrix of numbers
		2D numpy matrix
	'''

if __name__ == "__main__":
	print('Test')
	x = np.array([[1,2,3],[4,5,6]], np.int32)
	start_time = time.time()
	binary_search_2d(x)
	end_time = time.time()
	print("Runtime: {}s". format(end_time - start_time))