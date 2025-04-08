class Solution:
    def isPalindrome(self, x: int) -> bool:
        newstr = str(x)
        if newstr == newstr[::-1]:
            return True 
        return False
        
            