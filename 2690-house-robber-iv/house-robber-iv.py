class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def can_rob_with_capability(cap):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= cap:  # Can rob this house
                    count += 1
                    i += 1  # Skip the adjacent house
                i += 1
            return count >= k  # We need to rob at least k houses
        
        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right) // 2
            if can_rob_with_capability(mid):
                right = mid  # Try a lower capability
            else:
                left = mid + 1  # Increase capability since k houses weren't robbed
        
        return left  # This is the minimum possible capability