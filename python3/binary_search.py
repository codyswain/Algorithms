# Created by Cody Swain 

# Recursive binary search 
# Input: ordered list, number
# Output: index of number in ordered list (if exists)
# Complexity: log(n). The recursive stack includes at most log(n) function calls. 

def binary_search(list, num):
	if len(list) == 0:
		return None
	middle = int(len(list)/2)
	if list[middle] == num:
		return middle
	elif list[middle] < num:
		return middle + binary_search(list[middle:], num)
	elif list[middle] > num: 
		return binary_search(list[:middle], num)

def test_binary_search():
	test_arr = [0, 13, 17, 19, 22, 302, 467, 980, 1000, 1001, 1002, 1040]
	assert binary_search(test_arr, 0) == 0
	assert binary_search(test_arr, 19) == 3
	assert binary_search(test_arr, 980) == 7
	assert binary_search(test_arr, 1040) == len(test_arr)-1
	print("Test cases successful. Exiting... ")

if __name__ == "__main__":
	test_binary_search()