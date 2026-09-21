class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"]":"[","}":"{",")":"("}
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if stack and d[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
            