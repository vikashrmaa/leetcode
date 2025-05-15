class Solution(object):
    def isAnagram(self, s, t):
        countT = {}
        countS = {}
        for i in s:
            countS[i] = 1 + countS.get(i, 0)
        for j in t:
            countT[j] = 1 + countT.get(j, 0)
        if countT == countS:
            return True
        else:
            return False 

