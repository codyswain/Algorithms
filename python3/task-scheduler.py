'''Cody Swain
Leetcode Problem: #621 Task Scheduler'''

import collections # For creating frequency dict from list
import heapq # For Priority Queue
from typing import List # For typing annotation


class Solution:
	def cycle_counter(self, tasks: List[str], n: int) -> int:
		freq = collections.Counter(tasks)
		h = [-num for num in freq.values()] # Negative for heapq max heap
		heapq.heapify(h) # Create max heap

		cycles = 0
		temp_list = []
		
		while h: # If h is not empty
			cooldown_counter = n
			temp_list = [] 
			while cooldown_counter >= 0:
				cycles += 1
				if h:
					num = heapq.heappop(h)
					if num != -1:
						temp_list.append(num+1)
				if not h and not temp_list:
					break
				else:
					cooldown_counter -= 1
			for item in temp_list:
				heapq.heappush(h, item)

		return cycles
		

if __name__ == "__main__":
	tasks = ["A", "A", "A", "B", "B", "B"]
	cooldown = 2
	
	sol = Solution()
	cycles = sol.cycle_counter(tasks=tasks, n=cooldown)

	print(cycles) 
	
