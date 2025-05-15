class Solution(object):
    def containsDuplicate(self, nums):
        check = set()
        for i in nums:
            if i in check:
                return True
            else:
                check.add(i)
        return False