class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def canMakeZero(k: int) -> bool:
            n = len(nums)
            temp_nums = nums[:]  # Copy of nums
            diff = [0] * (n + 1)  # Difference array
            
            for i in range(k):
                l, r, val = queries[i]
                diff[l] -= val
                diff[r + 1] += val
            
            # Apply the difference array and check if nums can be made zero
            curr_decrement = 0
            for i in range(n):
                curr_decrement += diff[i]
                temp_nums[i] += curr_decrement  # Apply decrement
                if temp_nums[i] > 0:  # If still positive, return False
                    return False
            return True

        left, right = 0, len(queries)
        answer = -1

        while left <= right:
            mid = (left + right) // 2
            if canMakeZero(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer