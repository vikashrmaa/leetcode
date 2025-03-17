class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 != 0:
            return False 
        
        hashmap ={}
        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)
        for count in hashmap.values():
            if count % 2 != 0:
                return False 
        return True
                 

