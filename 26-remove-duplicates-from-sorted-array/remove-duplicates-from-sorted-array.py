class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr = [] #naya array banao but ans should be in the form of the existing list which is given with removing duplicates.
        for i in nums:
            if i not in arr:
                arr.append(i)
        nums[:] = arr #used to update the value of arr in the existing num
        return len(nums)

