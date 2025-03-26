from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten the grid into a 1D list
        nums = [num for row in grid for num in row]
        
        # Sort the numbers to find the median efficiently
        nums.sort()
        
        # Check if all elements can be converted to a common value
        remainder = [num % x for num in nums]
        if len(set(remainder)) > 1:
            return -1
        
        # Find the median value
        median = nums[len(nums) // 2]
        
        # Compute the total number of operations needed
        return sum(abs(num - median) // x for num in nums)