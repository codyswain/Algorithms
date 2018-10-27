__author__ = "Cody Swain"

class Solution(object):
	def merge(self, left_half, right_half, array):
		i=0
		j=0
		k=0
		while i<len(left_half) and j<len(right_half):
			if left_half[i] < right_half[j]:
				array[k] = left_half[i]
				i += 1
			else:
				array[k] = right_half[j]
				j += 1
			k += 1

		while i < len(left_half):
			array[k] = left_half[i]
			i+=1
			k+=1

		while j < len(right_half):
			array[k] = right_half[j]
			j+=1
			k+=1

	def merge_sort(self, array):
		print("Splitting {}".format(array))
		if len(array) > 1:
			mid = len(array) // 2
			left_half = array[:mid]
			right_half = array[mid:]
			self.merge_sort(left_half)
			self.merge_sort(right_half)
			self.merge(left_half, right_half, array)
		print("Merging {}".format(array))


if __name__ == "__main__":
	test_array = [6,2,9,7,1,6,8,11,35,75]
	Solution().merge_sort(test_array)
	print(test_array)