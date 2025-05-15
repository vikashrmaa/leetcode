class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in numset:
            # Only start when it's the beginning of a sequence
            if num - 1 not in numset:
                length = 1
                while num + length in numset:
                    length += 1
                longest = max(longest, length)

        return longest

