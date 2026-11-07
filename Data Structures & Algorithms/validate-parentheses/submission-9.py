class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        converse = {'(':')','{':'}','[':']'}

        for i in s:
            if i in converse.keys():
                stack.append(i)
            elif i in converse.values():
                if stack:
                    char = stack.pop()
                    if converse[char] != i:
                        return False
                else:
                    return False
        return True if not stack else False