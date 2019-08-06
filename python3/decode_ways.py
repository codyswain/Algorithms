class Solution:
    def num_decodings(self, s: str) -> int:
        # A table called count is used to store the results of subproblems
        count = [0] * (len(s)+1) #initializes an empty list of n+1 length
        count[0] = 1
        count[1] = 1 if s[0] != '0' else 0

        for i in range(2, len(s)+1):
            count[i] = 0

            # If the last digit is not 0
            # then the last digit must add to the number of words
            if (int(s[i-1]) > 0):
                count[i] = count[i-1]

            # If the second last digit is smaller than 2
            # and the last digit is smaller than 7
            # The digit forms a valid character
            if (int(s[i-2]) == 1 or (int(s[i-2]) == 2 and int(s[i-1]) < 7)):
                count[i] += count[i-2]
        return count[len(s)]

if __name__ == "__main__":
	encoded_str = "12543241"
	sol = Solution()

	sol_count = sol.num_decodings(encoded_str)
	print("Number of solutions for string {}: {}".format(encoded_str, sol_count))
