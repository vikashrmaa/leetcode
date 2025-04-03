class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0  # There must be at least 3 elements
        
        max_value = 0  # Stores the maximum result

        # Track the maximum value of (nums[i] - nums[j]) before any k
        max_diff = float('-inf')

        # Track the max nums[i] encountered so far
        max_i = nums[0]

        for j in range(1, n - 1):  # j is the middle element
            # Compute the best difference so far
            max_diff = max(max_diff, max_i - nums[j])

            # Pick the best k (which is simply nums[k] as we iterate)
            max_value = max(max_value, max_diff * nums[j + 1])

            # Update max_i (since i must be before j)
            max_i = max(max_i, nums[j])

        return max_value
