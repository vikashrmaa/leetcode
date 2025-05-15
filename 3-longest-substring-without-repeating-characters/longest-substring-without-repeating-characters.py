class Solution(object):
    def lengthOfLongestSubstring(self, s):
        check = set()
        ans = 0
        l = 0
        for r in range(len(s)):
            while s[r] in check:
                check.remove(s[l])
                l+=1 
            ans = max(ans, r-l + 1) 
            check.add(s[r])
        return ans       