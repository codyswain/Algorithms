__author__ = "Cody Swain"

class Solution(object):
	def get_total_word_count(self, str):
		return len(str.split())

	def get_word_frequency(self, str):
		word_dict = {}
		for word in str.split():
			if word in word_dict:
				word_dict[word] = word_dict[word] + 1
			else: 
				word_dict[word] = 1
		return word_dict

	def get_avg_word_length(self, str):
		counter = 0.0
		total = 0.0
		for word in str.split():
			counter += 1
			total += len(word)
		return total/counter

	def get_substring_frequency(self, substring, str):
		return str.count(substring)

if __name__ == "__main__":
	test_string = "hi my name is john and I want to say hi and hi"
	print("Total word count: {}".format(Solution().get_total_word_count(test_string)))
	print("Word frequency: {}".format(Solution().get_word_frequency(test_string)))
	print("Average word length: {}".format(Solution().get_avg_word_length(test_string)))
	print("Substring frequency: {}".format(Solution().get_substring_frequency("and", test_string)))
