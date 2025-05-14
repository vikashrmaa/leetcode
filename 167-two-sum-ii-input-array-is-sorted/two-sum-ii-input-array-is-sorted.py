class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers) #lem of number in n
        l = 0   # L will be at 0th position in array
        r = n - 1  #to put r at the last position of an array
        while l < r: #loop will work untill l < r
            if numbers[l] + numbers[r] < target: 
                l = l + 1
            elif numbers[l] + numbers[r] > target:
                r = r - 1
            else:
                return [ l + 1 , r + 1 ]


