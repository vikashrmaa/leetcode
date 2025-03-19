class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        subsets = []

        def dfs(i):

            if i >= n:
                res.append(subsets.copy())
                return 
            
            subsets.append(nums[i])
            dfs(i + 1)

            subsets.pop()
            dfs(i+1)

        dfs(0)

        return res



