class Solution:
    def isValid(self, s: str) -> bool:
        map = { ")":"(", "]":"[", "}":"{" }
        stack = []
        for i in s:
            if i in map:
                if stack and stack[-1] == map[i]:
                    stack.pop()
                else:   
                    return False  
            else:
                stack.append(i)
        return True if not stack else False
