class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        array = []
        for i in range(len(nums) - k, len(nums)):
            array.append(nums[i])  
        for i in range(len(nums) - k):
            array.append(nums[i])  
        for i in range(len(nums)):
            nums[i] = array[i]

