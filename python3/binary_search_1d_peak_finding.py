__author__ = "Cody Swain"

import time
import math

'''
In Python, all variables are passed by reference. 
This allows recursive function calls for binary search peak finding. 
'''
def measure_time(method):
	def timed(*args, **kwargs):
		st = time.time()
		result = method(*args, **kwargs)
		et = time.time()
		print("{s1} took {s2} seconds".format(s1=method.__name__, s2=et-st))
		return result
	return timed

@measure_time
def binary_search_1d_ver1(arr):
	'''Recursive binary search peak finding, slicing array indices. '''
	print("Length: {len} \t Array: {arr}".format(arr=arr, len=len(arr)))

	# Algorithm Implementation
	n = len(arr)
	if n%2 == 0:
		mid_idx = int(n/2-1)
	else: 
		mid_idx = int((n-1)/2)
	if arr[mid_idx] < arr[mid_idx-1]:
		return binary_search_1d_ver1(arr[:mid_idx])
	elif arr[mid_idx] < arr[mid_idx+1]:
		return binary_search_1d_ver1(arr[mid_idx:])
	else: 
		peak = arr[mid_idx]
		return peak

@measure_time
def binary_search_1d_ver2(arr):
	'''Non-recursive binary search. '''
	mid = None
	pos1 = 0
	pos2 = len(arr) - 1
	while True:
		if (pos1+pos2)%2 == 0:
			mid = int((pos1+pos2)/2)
		else:
			mid = int((pos1+pos2)/2-1)
		if arr[mid] > arr[mid-1] and arr[mid] < arr[mid+1]:
			pos1 = mid
		elif arr[mid] > arr[mid+1] and arr[mid] < arr[mid-1]:
			pos2 = mid
		else: 
			return array[mid]
			break

# def timeit(method):
#     def timed(*args, **kw):
#         ts = time.time()
#         result = method(*args, **kw)
#         te = time.time()
#         if 'log_time' in kw:
#             name = kw.get('log_name', method.__name__.upper())
#             kw['log_time'][name] = int((te - ts) * 1000)
#         else:
#             print '%r  %2.2f ms' % \
#                   (method.__name__, (te - ts) * 1000)
#         return result
#     return timed


if __name__ == "__main__":
	array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 18, 16, 14, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
	peak = binary_search_1d_ver1(array)
	print("\nPeak found: {}".format(peak))
	peak = binary_search_1d_ver2(array)
	print("\nPeak found: {}".format(peak))