class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(index, current_xor):
        # If we've considered all elements, add the XOR total to the result
            if index == len(nums):
                return current_xor
        
            with_element = backtrack(index + 1, current_xor ^ nums[index])
            # Case 2: Exclude nums[index] from the subset
            without_element = backtrack(index + 1, current_xor)
            # Return total XOR sum of both choices
            return with_element + without_element

        return backtrack(0, 0)


        
            

